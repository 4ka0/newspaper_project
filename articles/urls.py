from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView,
)


'''
To edit and delete articles we need new urls, views, and templates. For the
urls we can take advantage of the fact that Django automatically adds a primary
key to each database. Therefore our first article with a primary key of 1 will
be at articles/1/edit/ and the delete route will be at articles/1/delete/.
'''

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/newcomment', CommentCreateView.as_view(), name='comment_new'),
    path('', ArticleListView.as_view(), name='article_list')
]