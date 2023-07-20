""" This file defines the URL patterns for your web application. 
    It acts as a mapping between the URLs requested by clients and the corresponding view functions.
"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('home/', views.Home, name='home'), 
    path('logout/', views.LogOut, name='logout')
]
