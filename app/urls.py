from django.urls import path, include
from rest_framework_nested import routers
from app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'todos', views.TodoListViewSet, basename='user-todos')

urlpatterns = [
    path(r'api/',
         include(router.urls)),
    path(r'api/',
         include(users_router.urls)),
    path(r'api/psw_retrieve',
         views.PasswordRetrieveViewSet.as_view({'post': 'create'})),
    path(r'api/auth/',
         include('rest_auth.urls')),
]
