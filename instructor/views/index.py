from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication

#instructor index page
def index(request):
    name = request.session['instructoruser']['insName']
    context = {"name":name}
    return render(request, 'instructor/index.html',context)



