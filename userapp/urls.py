from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from . import views


urlpatterns = [
    path('auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    url('^linkedin/login/', OAuth2LoginView.adapter_view(views.CustomOAuth2Adapter)),
    url('^linkedin/login/callback/', OAuth2CallbackView.adapter_view(views.CustomOAuth2Adapter)),
]
