from django.shortcuts import render
from projects.models import Project


def dashboard_view(request):
    # try:
        context = {
                'latest_projects' : Project.objects.all().order_by('-created_at')[:5]

        }
        return render(request,'dashboard/dashboard.html', context)
    # except Exception as e:
    #     return render(request, 'error.html')