from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    queryset = Article.objects.order_by('-date')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body', 'image')
    template_name = 'article_edit.html'
    login_url = 'login'

    # Test to see if the current user is the author of the current article.
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


'''
Uses LoginRequiredMixin to restrict access to this view to only users who are
logged in. Necessary to include LoginRequiredMixin before CreateView.
'''
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'image')
    login_url = 'login'  # overrides the default login url which is /accounts/login

    # Automatically sets the current user as the author of the new article
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_article.html', {'form': form})