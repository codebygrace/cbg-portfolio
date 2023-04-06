from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'projects/index.html')

def projects(request):
    projects = Project.objects.all()
    count = projects.count()
    context = {
        'count': count,
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)

