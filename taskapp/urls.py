from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='list_create'),
    path('<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='retrieve_update_delete')
]