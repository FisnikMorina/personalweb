from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def project(request):
    return render(request=request, template_name='personalpage/projects.html', context={"project":project})