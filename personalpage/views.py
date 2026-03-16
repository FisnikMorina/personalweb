from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def home(request):
    response = Project.objects.order_by("pub_date")
    return render(request=request, template_name="personalpage/home.html",context={"response":response})

def project(request):
    projects = Project.objects.order_by('pub_date')
    return render(request=request, template_name='personalpage/projects.html', context={"projects":projects})