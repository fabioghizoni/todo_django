from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from app.serializers import UserSerializer
from app.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif (self.action == 'retrieve'
              or self.action == 'update'
              or self.action == 'destroy'
              or self.action == 'partial_update'):
            permission_classes = [IsLoggedInUserOrAdmin]
        elif (self.action == 'list'):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
