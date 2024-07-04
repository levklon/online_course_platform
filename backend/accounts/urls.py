from django.urls import path
from .views import RegisterAPI, CustomAuthToken

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
]
