from django.contrib import admin
from django.urls import path, include
from . import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', include('store.urls')),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
