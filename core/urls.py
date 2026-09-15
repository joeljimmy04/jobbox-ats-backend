from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from .views import JobListAPI

urlpatterns = [
    path("", views.home, name='home'),
    path("jobs/", JobListAPI.as_view(), name='job-list'),
    path("create/", views.JobCreateAPI.as_view(), name='job-create')
]