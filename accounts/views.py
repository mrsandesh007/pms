from django.shortcuts import render
from projects.models import Project
from tasks.models import Task
from.models import UserProfile
from notification.models import Notification


def dashboard_view(request):
    # try:
        latest_notifications = Notification.objects.filter(receiver=request.user)[:3]

        context = {
            'latest_projects' : Project.objects.all()[:5],
            'latest_tasks' : Task.objects.all()[:5],
            'latest_members' : UserProfile.objects.all()[:5],
            'latest_notifications' : latest_notifications,
            'notification_count' : latest_notifications.count()

        }
        return render(request,'dashboard/dashboard.html', context)
    # except Exception as e:
    #     return render(request, 'error.html')