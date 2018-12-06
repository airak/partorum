from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="index.html"), name="login"),
    path('sair/', auth_views.LogoutView.as_view(next_page="core:login"), name="logout"),
]