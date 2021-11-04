from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication



def editProfile(request):
    name = request.session['instructoruser']['insName']
    try:
        id = request.session['instructoruser']['iid']
        obj = instructor.objects.get(iid = id)
        context = {"ins" : obj,"name":name}
        return render(request, "instructor/profile/editProfile.html", context)
    except:
        context = {"info" : "Error edit instructor!","name":name}
        return render(request, "instructor/profile/profileInfo.html", context)

def updateProfile(request):
    name = request.session['instructoruser']['insName']
    context = {"name":name}
    try:
        id = request.session['instructoruser']['iid']
        obj = instructor.objects.get(iid = id)
        obj.username = request.POST['username']
        obj.pw = request.POST['password']
        obj.name = request.POST['name']
        obj.gender = request.POST['gender']
        obj.email = request.POST['email']
        stat = request.POST.get('status')

        if stat == 'S':
            obj.curStatus = 0
        else:
            obj.curStatus = 1
        obj.save()

        context = {"info" : "Edit instructor success!","name":name}
    except:
        context = {"info" : "Edit instructor fail!","name":name}
    return render(request, "instructor/profile/profileInfo.html", context)

