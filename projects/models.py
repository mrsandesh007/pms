from django.db import models
import uuid


STATUS_CHOICES = [
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),

    
]
PRIORITY_CHOICES =[
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),


]

class Project(models.Model):
    id             = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name           = models.CharField(max_length=100)
    description    = models.TextField(blank=True, null=True)
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")
    priority       = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    is_active      = models.BooleanField(default=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def priority_color(self):
        if self.priority == "Low":
            color = "success"
        elif self.priority == "Medium":
            color = "warning"
        else:
            color = "danger"

        return color
            


