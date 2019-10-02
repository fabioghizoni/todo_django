from django.urls import path, include
from rest_framework import routers
from app import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
# router.register('psw_retrieve',
                # views.PasswordRetrieveViewSet,
                # basename=)

urlpatterns = [
    path('api/',
         include(router.urls)),
    path('api/psw_retrieve',
         views.PasswordRetrieveViewSet.as_view({'post': 'create'})),
    path('api/auth/',
         include('rest_auth.urls')),
]
