from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timesince import timesince


class UserProfile(models.Model):
    user             = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture  = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio              = models.TextField(null=True, blank=True)
    address          = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth    = models.DateField(null=True, blank=True)
    join_date        = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    
    @property
    def profile_picture_url(self):
        try:
            image = self.profile_picture.url
        except:
            image = "https://imgs.search.brave.com/7-vItDe-hLZrFR1JxmHlNnbfim1kKYy6iLsDslP9s9A/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTcy/NjIxMzk5My92ZWN0/b3IvZGVmYXVsdC1h/dmF0YXItcHJvZmls/ZS1wbGFjZWhvbGRl/ci1hYnN0cmFjdC12/ZWN0b3Itc2lsaG91/ZXR0ZS1lbGVtZW50/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1uWWxrMGowNzZD/Qlo1eEdDQ2FWWHRJ/U1lHSzJTelhSd3VR/QlhQa2ZtTVg0PQ"

        return image
    
    @property
    def full_name(self):
        name = self.user.get_full_name()
        if name:
            return name
        return self.user.username
    
    @property
    def date_joined(self):
        value = timesince(self.user.date_joined)
        precise = value.split(",")[0]
        return f"{precise} ago"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance , **kwargs):
    UserProfile.objects.get_or_create(user=instance)

