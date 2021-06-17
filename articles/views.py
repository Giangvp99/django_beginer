from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/new.html"
    fields = (
        "title",
        "body",
    )
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/list.html"
    login_url = "login"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"
    login_url = "login"


class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "articles/edit.html"
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("articles:list")
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
