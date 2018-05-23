from django.contrib import admin

# Register your models here.
from .models import Theme, Video, Thumb, Comment

admin.site.register(Theme)
admin.site.register(Video)
admin.site.register(Thumb)
admin.site.register(Comment)