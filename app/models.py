from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        related_name='todos',
        on_delete=models.CASCADE
    )


class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(auto_now=True)
    todo_list = models.ForeignKey(
        TodoList,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.CASCADE
    )
