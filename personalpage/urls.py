from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='projects'),
    path('cv/', views.cv_download, name='cv_download')
]