from django.conf.urls import include, url
from django.contrib import admin
from django.urls.conf import path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url('signup/', views.signup, name='signup'),
    url('login/', views.user_login, name='login'),
    path('admin/', admin.site.urls),
    url('', include('yarr.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
