from .models import TaskModel
from .forms import TaskForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

class TaskListView(ListView):
    """
        View for listing all the task
    """
    context_object_name = 'task_list'
    queryset = TaskModel.objects.all()
    template_name = 'task_list.html'

class TaskCreateView(CreateView):
    """
        View for creating a task
    """
    model = TaskModel
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('list')

class TaskDetailView(DetailView):
    """
        View for Displyign a particular task
    """
    context_object_name = 'task'
    queryset = TaskModel.objects.all()
    template_name = 'task_detail.html'

class TaskUpdateView(UpdateView):
    """
        View for updating a task
    """
    model = TaskModel
    context_object_name = 'task'
    fields = '__all__'
    template_name = 'task_update.html'
    success_url = reverse_lazy('list')

class TaskDeleteView(DeleteView):
    """
        View for delete a task
    """
    model = TaskModel
    context_object_name = 'task'
    template_name = 'task_delete.html'
    success_url = reverse_lazy('list')