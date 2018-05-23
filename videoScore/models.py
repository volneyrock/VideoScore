from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=100)
    score = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    date_uploaded = models.DateField()
    views = models.IntegerField()
    themes = models.ManyToManyField(Theme)
       

    def __str__(self):
        return self.title


class Thumb(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    
class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    