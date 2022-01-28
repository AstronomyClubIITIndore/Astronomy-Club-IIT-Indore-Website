from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from astro import views


urlpatterns = [
    path('', views.home, name='home'), 

]
