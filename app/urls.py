from django.urls import path, include
from rest_framework import routers
from app import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('api/',
         include(router.urls)),
    path('api/auth/',
         include('rest_auth.urls')),
]
