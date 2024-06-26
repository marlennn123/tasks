from rest_framework import viewsets, permissions
from .serializers import TaskSerializers
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['completed']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



