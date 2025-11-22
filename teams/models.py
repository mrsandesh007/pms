from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name        = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    team_lead   = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_lead")
    members     = models.ManyToManyField(User, related_name="teams")
    Created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_teams")
    created_at  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    


