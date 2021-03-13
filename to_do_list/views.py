from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Task
from .serializers import TaskSerializer


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
