from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from taskapp.models import TaskModel
from .serializers import TaskSerializer


class TaskListCreateView(ListCreateAPIView):
    """
        Api class for listing all task and creating one task
    """
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
        Api class for retrieveing, updating and deleting a particular task
    """
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer