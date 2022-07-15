from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TaskModel
from .serializers import TaskSerializer

class TaskListCreateView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
