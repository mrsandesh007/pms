from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone


class NotificationManager(models.Manager):
    def for_user(self, user):
        return self.filter(receiver=user)
    

    def unread_notification(self, user):
        return self.for_user(user).filter(read=False)
    

    def read_notification(self, user):
        return self.for_user(user).filter(read=True)


class Notification(models.Model):
    sender          = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True, related_name="sent_notifications")
    receiver        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications")
    message         = models.CharField(max_length=255)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.CharField(max_length=255)
    content_object  = GenericForeignKey('content_type', 'object_id')

    created_at      = models.DateTimeField(default=timezone.now)
    is_read         = models.BooleanField(default=False)

    objects         = NotificationManager()


    def __str__(self):
        return f"{self.sender} {self.message} {self.content_object}"
    

    class Meta:
        ordering = ['-created_at']


    @property
    def notification_time_formatted(self):
        return self.created_at.strftime('%d %b %I: %M %p')
