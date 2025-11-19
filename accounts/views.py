from django.shortcuts import render
from projects.models import Project
from tasks.models import Task


def dashboard_view(request):
    # try:
        context = {
                'latest_projects' : Project.objects.all()[:5],
                'latest_tasks' : Task.objects.all()[:5]


        }
        return render(request,'dashboard/dashboard.html', context)
    # except Exception as e:
    #     return render(request, 'error.html')