from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from app.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id', 'url', 'user', 'title')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    email = serializers.EmailField(
        required=True,
    )
    todos = serializers.HyperlinkedIdentityField(
        many=True,
        view_name='user-todos-list',
        lookup_url_kwarg='user_pk'
    )

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'todos')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


