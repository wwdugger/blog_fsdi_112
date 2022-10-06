from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Status


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="published")
        context['post_list'] = Post.objects.filter(status=pending_status).order_by('created_on').reverse()

        return context

class DraftListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="draft")
        context['post_list'] = Post.objects.filter(status=pending_status).order_by('created_on').reverse()

        return context

class ArchivedListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="archived")
        context['post_list'] = Post.objects.filter(status=pending_status).order_by('created_on').reverse()

        return context

class SaleListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category="Products").order_by('created_on').reverse()
        return context

class ResourceListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category="Resources").order_by('created_on').reverse()
        return context

class ExperienceListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category="Experiences").order_by('created_on').reverse()
        return context

class TwinListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category="Twins").order_by('created_on').reverse()
        return context

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "body", "category"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name =  "posts/edit.html"
    model = Post
    fields = ["title", "body", "category"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user
