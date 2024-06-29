from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing tasks.

    Provides CRUD operations (Create, Retrieve, Update, Delete) for tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
