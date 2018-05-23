from django.shortcuts import render, redirect
from .models import Video, Thumb, Comment, Theme
from .forms import VideoForm, ThumbForm, CommentForm, ThemeForm
from datetime import date

# Create your views here.
def index(request):
    '''
    List all videos
    '''
    data = {}
    data['videos'] = Video.objects.all()
   
    return render(request, 'videoScore/index.html', data)


def get_popular_themes(request):
    '''
    Update and get popular themes by score
    '''
    data = {}
    themes_data = {}
    themes = Theme.objects.all()
    for t in themes:
        theme_score = 0
        video = Video.objects.filter(themes=t.id)
        for v in video:
            video_score = videoScore(v.id, v.date_uploaded, v.views)
            theme_score += video_score

        t.score = theme_score
        t.save()

    data['themes'] = Theme.objects.all().order_by('-score')

    return render(request, 'videoScore/popular_themes.html', data)


def videoScore(v_id, date_uploaded, views):
    '''
    Calculate the video score function
    '''
    Score = 0
    thumbs_up = Thumb.objects.filter(is_positive=True, video=v_id).count()
    thumbs_down = Thumb.objects.filter(is_positive=False, video=v_id).count()
    try:
        ThumbsUp = thumbs_up/(thumbs_up+thumbs_down)
    except ZeroDivisionError:
        ThumbsUp = 0
    # Positive Comments
    positive_comments = Comment.objects.filter(is_positive=True, video=v_id).count()
    negative_comments = Comment.objects.filter(is_positive=False, video=v_id).count()
    try:
        GoodComments = positive_comments/(positive_comments+negative_comments)
    except ZeroDivisionError:
        GoodComments = 0
    # Positive Factor
    PositivityFactor = 0.7 * GoodComments + 0.3 * ThumbsUp
    # Time factor
    today = date.today()
    days_since_upload = abs(date_uploaded - today)
    TimeFactor = max(0, 1 - (days_since_upload.days/365))
    #VideoScore
    Score = views * TimeFactor * PositivityFactor

    return Score


def new_video(request):
    '''
    Insert a new video
    '''   
    form = VideoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'videoScore/new.html', {'form':form})

def new_thumb(request):
    '''
    Insert a new thumb
    '''   
    form = ThumbForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'videoScore/new.html', {'form':form})


def new_comment(request):
    '''
    Insert a new comment
    '''   
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'videoScore/new.html', {'form':form})


def new_theme(request):
    '''
    Insert a theme
    '''   
    form = ThemeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'videoScore/new.html', {'form':form})


def edit_video(request, pk):
    '''
    Edit a video by id
    '''
    data = {}
    video = Video.objects.get(pk=pk)
    form = VideoForm(request.POST or None, instance=video)

    if form.is_valid():
        form.save()
        return redirect('index')

    data['video'] = video
    data['form'] = form

    return render(request, 'videoScore/new_video.html', data)

def delete_video(request, pk):
    '''
    Delete a video by id
    '''
    video = Video.objects.get(pk=pk)
    video.delete()
    return redirect('index')
