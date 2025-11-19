from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user             = models.OneToOneField(User, on_delete=models.CASCADE)
    bio              = models.TextField(null=True, blank=True)
    address          = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth    = models.DateField(null=True, blank=True)
    join_date        = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
