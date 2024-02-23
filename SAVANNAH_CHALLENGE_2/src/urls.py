from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/', include('SAVANNAH_CHALLENGE_2')),
    
]