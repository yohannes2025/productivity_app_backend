# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'activities', views.ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
