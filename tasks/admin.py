from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "owner", "status", "priority", "start_date", "due_date")
    search_fields = ("name", "description")
    list_filter = ("status", "priority", "project", "owner")

