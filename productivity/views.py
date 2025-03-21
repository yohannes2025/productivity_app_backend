# views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import User, Task, Comment, Activity
from .serializers import UserSerializer, TaskSerializer, CommentSerializer, ActivitySerializer
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = self.queryset
        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if category:
            queryset = queryset.filter(category=category)
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        task_id = self.request.query_params.get('task_id')

        if task_id:
            queryset = queryset.filter(task_id=task_id)

        return queryset
