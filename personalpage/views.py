from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from django.conf import settings
import os

from .models import Project, CVDownload


STATIC_PATH = os.path.join(settings.BASE_DIR,'personalpage','static','personalpage')

def home(request):
    response = Project.objects.order_by("pub_date")
    return render(request=request, template_name="personalpage/home.html",context={"response":response})

def project(request):
    projects = Project.objects.order_by('pub_date')
    return render(request=request, template_name='personalpage/projects.html', context={"projects":projects})

def cv_download(request):
    lang = request.GET.get('lang')
    filename = 'Fisnik_Morina_CV_N.pdf' if lang=='en' else 'Fisnik_Morina_Lebenslauf_DE.pdf'
    filepath = os.path.join(STATIC_PATH, filename)

    CVDownload.objects.create()

    response = FileResponse(open(filepath,'rb'))
    return response