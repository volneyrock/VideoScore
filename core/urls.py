"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from videoScore.views import index, edit_video, delete_video
from videoScore.views import new_theme, new_video, new_thumb, new_comment
from videoScore.views import get_popular_themes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('new_theme/', new_theme, name='new_theme'),
    path('new_video/', new_video, name='new_video'),
    path('new_thumb/', new_thumb, name='new_thumb'),
    path('new_comment/', new_comment, name='new_comment'),
    path('edit_video/<int:pk>', edit_video, name='edit_video'),
    path('delete_video/<int:pk>', delete_video, name='delete_video'),
    path('get_popular_themes', get_popular_themes, name='popular_themes'),
]
