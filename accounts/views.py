from django.shortcuts import render
from projects.models import Project
from tasks.models import Task
from.models import UserProfile
from notification.models import Notification
from teams.models import Team


def dashboard_view(request):

    if request.user.is_authenticated:
        latest_notifications = Notification.objects.for_user(request.user)[:3]
        notification_count = latest_notifications.count()
    else:
        latest_notifications = []
        notification_count = 0

    context = {
        'latest_notifications': latest_notifications[:3],
        'notification_count': notification_count,
        'latest_projects': Project.objects.all()[:5],
        'project_count': Project.objects.count(),

        'latest_tasks': Task.objects.all()[:5],
        'tasks_count': Task.objects.count(),

        'latest_members': UserProfile.objects.all()[:8],
        'members_count': UserProfile.objects.count(),
        'team_count' : Team.objects.count()

    }

    return render(request, 'dashboard/dashboard.html', context)
