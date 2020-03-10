from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('auth/google/', views.GoogleLogin.as_view(), name='google_login'),
]
