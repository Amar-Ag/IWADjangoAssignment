from django.shortcuts import render

from django.views.generic import ListView, DetailView, DeleteView
from .models import BlogArticle, Author


def homePage(request):
    return render(request, 'blog/index.html', context=None)


class BlogsList(ListView):
    queryset = BlogArticle.objects.all().order_by('-created_at')
    context_object_name = 'blogs'
    template_name = 'blog/blogs.html'
    paginate_by = 3


class BlogsDetail(DetailView):
    model = BlogArticle
    pk_url_kwarg = 'id'
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'


class AuthorList(ListView):
    queryset = Author.objects.all().order_by('name')
    context_object_name = 'authors'
    template_name = 'blog/authors.html'
    paginate_by = 3
