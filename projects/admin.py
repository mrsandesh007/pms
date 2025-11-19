from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "status", "priority", "start_date", "due_date", "is_active")
    search_fields = ("name", "description")
    list_filter = ("status", "priority", "owner", "is_active")
