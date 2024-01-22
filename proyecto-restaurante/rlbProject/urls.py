"""rlbProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rlbApp import views
from rlbApp.views import userCreateView
from rlbApp.views import menuListView
from rlbApp.views import platoDetailView
from rlbApp.views import userDetailView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('create-user/', views.UserCreateView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('list-menu/', views.MenuListView.as_view()),
    path('create-plato/', views.PlatoCreateView.as_view()),
    path('plato-dia/', views.PlatoDetailView.as_view()),
    path('create-reserva/', views.ReservaCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view())
]
