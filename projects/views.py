from django.shortcuts import render


def create_project(request):
    return render(request, "project/form.html")