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
    url('logout/', views.user_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('catalogue/', views.catalogue),
    url('', include('yarr.urls')),

]

urlpatterns += staticfiles_urlpatterns()
