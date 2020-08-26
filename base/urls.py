from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('users/', include('users.urls')),  # To include the users app at the '/users' url
    path('users/', include('django.contrib.auth.urls')),  # To include the built-in auth app (has its own urls for login and logout)
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
