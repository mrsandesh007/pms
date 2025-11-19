from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "address", "date_of_birth", "join_date")
    search_fields = ("user__username", "address")
    list_filter = ("join_date",)
