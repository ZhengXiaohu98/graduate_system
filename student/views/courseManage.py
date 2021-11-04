from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student, schedules, instructor, course
from django.http import HttpResponse

def index(request):
    pass