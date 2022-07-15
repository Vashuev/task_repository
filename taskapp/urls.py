from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
]