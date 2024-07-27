from django.contrib import admin
from django.urls import path, include
from . import settings
import the_weather.weather.urls
from . views import user_login, user_logout, user_signup


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('weather/', include(the_weather.weather.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
