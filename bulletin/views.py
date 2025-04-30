from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import (UpdateView, DeleteView)

from .models import Post
from .admin import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = "home.html" 


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class BulletinView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "bulletin.html" 


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = (
        "title",
        "tag",
        "body",
    )
    template_name = "post_edit.html"
    success_url = reverse_lazy("bulletin")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("bulletin")

    def test_func(self):
        obj = self.get_object()
        return (obj.author == self.request.user) or (self.request.user.is_manager)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = (
        "title",
        "tag",
        "body")
    success_url = reverse_lazy("bulletin")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)