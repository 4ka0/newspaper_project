from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    '''
    This is the page that is shown after a new article has been added.
    In this case the page shown is the detail view of the new article.
    '''
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(
        'articles.Article',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
