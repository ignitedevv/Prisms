from django.contrib import admin
from django.urls import path
from . import views

app_name = "Prisms"


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

]

