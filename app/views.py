from django.utils import timezone
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app.models import TodoList
from app.serializers import (
    UserSerializer,
    TodoListSerializer
)
from app.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class TodoListViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        user = get_object_or_404(User, pk=user_pk)
        queryset = TodoList.objects.filter(user=user)
        serializer = TodoListSerializer(
            queryset,
            context={'request': request},
            many=True
        )
        return Response(serializer.data)

    def create(self, request, user_pk=None):
        user = get_object_or_404(User, pk=user_pk)

        todo_list = TodoList.objects.create(
            title=request.data['title'],
            user_id=user_pk
        )

        return Response(todo_list, status=status.HTTP_201_CREATED)


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


class PasswordRetrieveViewSet(viewsets.ViewSet):

    permission_classes = [AllowAny]

    def create(self, request):
        user = get_object_or_404(User, username=request.data['username'])

        password = password_generator()
        subject = 'New Password from todo_django'
        message = 'Your new password is: ' + password
        to = [str(user.email)]

        try:
            send_mail_default(subject, message, to)
            user.set_password(password)
            user.save()
            content = {'detail': 'new password sent to ' + str(user.email)}
            return Response(content)
        except:
            content = {'detail': 'could not send to ' + str(user.email)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


def send_mail_default(subject, message, to, file=None):
    email = EmailMessage(subject,
                         message,
                         'django@todolist.com',
                         to,)
    return email.send(fail_silently=False)


def password_generator():
    date = timezone.localtime()
    x = int(date.strftime('%d'))*2
    xx = str(x) if x > 9 else '0' + str(x)
    y = int(date.strftime('%m'))*2
    yy = str(y) if y > 9 else '0' + str(y)
    password = xx + yy + date.strftime('%H')

    return password

