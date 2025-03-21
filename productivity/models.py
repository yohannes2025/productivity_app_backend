# models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    """Model for tasks."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_overdue = models.BooleanField(default=False)
    priority = models.IntegerField(
        choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[
        ('open', 'Open'), ('in_progress', 'In Progress'), ('done', 'Done')])
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """Model for task comments."""
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    """Model for task activity logs."""
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
