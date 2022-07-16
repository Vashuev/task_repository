from django.db import models

class TaskModel(models.Model):
    Priority_choices = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    name = models.CharField(unique=True, max_length=255)
    priority = models.CharField(choices=Priority_choices, max_length=6)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name