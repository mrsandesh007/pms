from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "message", "content_object", "created_at", "is_read")
    list_filter = ("is_read", "created_at", "sender", "receiver")
    search_fields = ("message", "sender__username", "receiver__username")
