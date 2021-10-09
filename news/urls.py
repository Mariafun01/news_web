from django.contrib import admin
from django.urls import path

from news import views, api_views

app_name='news'


urlpatterns = [
    path('index/', views.index, name='index'),
    path('newslist/<int:id>/', views.newslist, name='newslist', ),
    path('news/<int:id>/', views.news, name="news"),
    path('news/api/fav/<int:id>/',api_views.api_fav,name='api_fav'),
    path('newsdetail/', views.newsdetail, name='newsdetail'),
    path('upload_comment/', views.upload_comment, name="upload_comment"),
]