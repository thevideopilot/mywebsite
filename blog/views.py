from django.shortcuts import render
from .models import Post, Resume
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    # default template : <app>/<model>_<viewtype>.html



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def resume(request):
    context = {
        'resumes': Resume.objects.all()
    }
    return render(request, 'blog/resume.html', context)


class ResumeListView(ListView):
    model = Resume
    template_name = 'blog/resume.html'
    context_object_name = 'resumes'

