from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.post, name="about"),
    path('posts/', views.posts, name="posts"),
    path('profile/', views.profile, name="profile"),
]
