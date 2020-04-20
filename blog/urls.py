from django.urls import path
from .views import PostListView, PostDetailView, ResumeListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('resume/', ResumeListView.as_view(), name='blog-resume')
]