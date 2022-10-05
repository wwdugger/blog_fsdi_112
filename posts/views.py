from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from posts.models import Post

class HomePage(TemplateView):
    template_name = "posts/home.html"

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/create.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]

