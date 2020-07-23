from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    '''
    The next line links the comment model to the article model through the use
    of a foreign key, and also sets a many-to-one relationship from the comment
    model to te article model. It requires two positional arguments: the other
    model to which this model is related and the on_delete option.
    '''
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'  # Used in the template, in the template {% for comment in article.comments.all %}
    )

    '''
    This line links the comment model to the custom user model in a similar
    manner to the above.
    '''
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    comment = models.CharField(max_length=140)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
