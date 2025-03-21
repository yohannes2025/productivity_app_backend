# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model that extends the default Django User model.
    Includes additional fields for user profile management.
    """
    email = models.EmailField(unique=True)
    # Add any other custom fields here


class Task(models.Model):
    """
    Model to represent a user's task.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_overdue = models.BooleanField(default=False)
    priority = models.IntegerField(
        choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[(
        'open', 'Open'), ('in_progress', 'In Progress'), ('done', 'Done')])
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    Model to represent a comment on a task.
    """
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    """
    Model to represent an activity related to a task.
    """
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
