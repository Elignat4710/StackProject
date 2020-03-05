from django.urls import path
from .views import Registration


app_name = 'user'

urlpatterns = [
    path('register/', Registration.as_view())
]