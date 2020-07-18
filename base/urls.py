"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    # For the admin page
    path('admin/', admin.site.urls),
    # To include the pages app
    path('', include('pages.urls')),
    # To include the users app from the '/users' url
    path('users/', include('users.urls')),
    # To include the built-in auth app (has its own urls for login and logout)
    path('users/', include('django.contrib.auth.urls')),

]
