"""videopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('a/',views.index,name='index'),
    path('',views.video_view,name="video"),
    path('score/',views.score_view,name="score"),
    path('rank/',views.rank_view,name="rank"),
    path('user_rank/<int:id>',views.user_rank,name="userrank"),
    path('register/',views.user_view,name="register"),
    path('login/',views.login,name="login"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
