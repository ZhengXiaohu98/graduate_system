from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication

def insApplications(request):
    return render(request, 'instructor/ins_application.html')

def saveApplication(request):
    id = request.POST.get('id', None)
    insName = request.POST.get('name', None)
    gender = request.POST.get('gender', None)
    email = request.POST.get('email', None)
    extraInfo = request.POST.get('extraInfo', None)
    if id is None or insName is None or gender is None or email is None:
        return render(request, 'instructor/info.html', {"info":"You must fill the requiered field!"})
    obj = insApplication()
    obj.stateid = id
    obj.insName = insName
    obj.gender = gender
    obj.email = email
    obj.info = extraInfo
    obj.save()
    return render(request, 'instructor/info.html', {"info":"Applied successfully! You can use your state ID to check your application!"})

def checkApplication(request):
    return render(request, 'instructor/ins_application_check.html', {'info':''})

def docheckApplication(request):
    id = request.POST['id']
    try:
        obj = insApplication.objects.get(stateid = id)
    except:
        return render(request, 'instructor/ins_application_check.html', {'info':'No application found!'})
    return render(request, 'instructor/ins_application_status.html', {'insApp':obj})