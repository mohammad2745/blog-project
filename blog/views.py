from django.shortcuts import render
from .models import Post
from django.views import generic


class BlogListView(generic.ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
