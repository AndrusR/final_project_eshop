from django.contrib import admin
from django.urls import path, include
from . import settings
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('store.urls')),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('mootor/', mootor, name='mootor'),
    path('purjekad/', purjekad, name='purjekad'),
    path('jetid/', jetid, name='jetid'),
    path('paaste/', paaste, name='paaste'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
