from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Video, Thumb, Comment, Theme
from datetime import date

class VideoForm(ModelForm):

    def clean_date_uploaded(self):
        '''
        Validate if date < one year
        '''
        date_uploaded = self.cleaned_data.get('date_uploaded')
        today = date.today()
        past = date.fromordinal(today.toordinal() - 365)# One year ago
        if date_uploaded < past:
            raise ValidationError("Video date can not be less than a year")
        return date_uploaded

    class Meta:
        model = Video
        fields = ['title', 'date_uploaded', 'views', 'themes']
 

class ThumbForm(ModelForm):

    class Meta:
        model = Thumb
        fields = ['is_positive', 'video']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['is_positive', 'video']

class ThemeForm(ModelForm):

    class Meta:
        model = Theme
        fields = ['name']