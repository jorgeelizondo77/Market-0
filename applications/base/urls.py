from django.urls import path
from django.contrib.auth import views as auth_views

from applications.base.views import Base

from .views import *

app_name = 'base'

urlpatterns = [
    path('',Base.as_view(), name='index'),
    
    # path('login/',auth_views.LoginView.as_view(template_name='base/login.html'),
    #     name='login'),

    # path('logout/',
    #      auth_views.LogoutView.as_view(template_name='base/login.html'),
    #      name='logout'),

    # path('sin_privilegios/',
    #      HomeSinPrivilegios.as_view(),
    #      name='sin_privilegios'),
    
]