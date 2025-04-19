from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ("title","body",)
    template_name = "article_edit.html"

class ArticleDeleteView(DeleteView): # new
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

class ArticleCreateView(CreateView): # new
    model = Article
    template_name = "article_new.html"
    fields = ("title","body","author",)


