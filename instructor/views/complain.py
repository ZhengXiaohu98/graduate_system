from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication, schedules, complainmsg, student, stuCourse

def editComplain(request):
    name = request.session['instructoruser']['insName']
    context = {"name":name}
    return render(request,"instructor/complain/newComplain.html",context)


def updateComplain(request):
    name = request.session['instructoruser']['insName']
    try:
        id = request.session['instructoruser']['iid']
        ins = instructor.objects.get(iid=id)
        objname = request.POST.get("complainName")
        obj = student.objects.get(stuName = objname)
        print(obj)
        complain = complainmsg()
        complain.sendType = "Instructor"
        complain.fromId = id
        complain.fromName = ins.insName
        complain.receiveType = "Student"
        complain.receiveId = obj.sid
        complain.receiveName = obj.stuName
        complain.save()
        context = {"info":"Complain Successfully!","name":name}
        return render(request,"instructor/complain/complainInfo.html",context)
    except:
        context = {"info":"Complain Failed! Make sure student name exists!","name":name}
        return render(request,"instructor/complain/complainInfo.html",context)