from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView


urlpatterns = [
    # For the admin page
    path('admin/', admin.site.urls),
    # To include the pages app
    path('', include('pages.urls')),
    # To include the users app from the '/users' url
    path('users/', include('users.urls')),
    # To include the built-in auth app (has its own urls for login and logout)
    path('users/', include('django.contrib.auth.urls')),
    # To include the articles app
    path('articles/', include('articles.urls')),
]
