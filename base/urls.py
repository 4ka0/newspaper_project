from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('users/', include('users.urls')),  # To include the users app at the '/users' url
    path('users/', include('django.contrib.auth.urls')),  # To include the built-in auth app (has its own urls for login and logout)
    path('articles/', include('articles.urls')),
]