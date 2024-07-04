from django.urls import path, include
from .views import RegisterAPI, CustomAuthToken
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, VideoViewSet
from .views import create_checkout_session

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
]


router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'videos', VideoViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += [
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
]
