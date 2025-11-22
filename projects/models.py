from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth import get_user_model
from teams.models import Team

User = get_user_model()


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


class ProjectQueryset(models.QuerySet):
    def active_projects(self):
        return self.filter(is_active=True)
    
    def due_expired_projects(self):
        return self.filter(due_date__gte=timezone.now())


class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQueryset(self.model, using=self._db)
    

    def all(self):
        return self.get_queryset().active_projects().due_expired_projects()
    

class Project(models.Model):
    id             = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team           = models.ForeignKey(Team, related_name="projects", on_delete=models.CASCADE)
    owner          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name           = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True, null=True)
    description    = models.TextField(blank=True, null=True)
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")
    priority       = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    start_date     = models.DateField()
    due_date       = models.DateField()
    is_active      = models.BooleanField(default=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    objects        = ProjectManager()


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']


    def days_until_due(self):
        if not self.due_date:
            return None

        today = timezone.now().date()
        days_left = (self.due_date - today).days

        # If due within 30 days
        if days_left <= 30:
            return f"Due in {days_left} days"

        # If more than 30 days → show formatted date
        return self.due_date.strftime("Due on %b %d") 


    @property
    def project_progress(self):
        progress_dict = {
            'To Do'        : 0,
            'In Progress'  : 50,
            'Completed'    : 100,
        }
        return progress_dict.get(self.status, 0)
    

    def project_progress_color(self):
        progress = self.project_progress
        if progress == 100:
            color = "success"
        elif progress == 50:
            color = "primary"
        else:
            color = ""

        return color


    
    def priority_color(self):
        if self.priority == "Low":
            color = "success"
        elif self.priority == "Medium":
            color = "warning"
        else:
            color = "danger"

        return color
            


