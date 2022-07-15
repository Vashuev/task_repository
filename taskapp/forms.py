from django.forms import ModelForm 
from .models import TaskModel

class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'