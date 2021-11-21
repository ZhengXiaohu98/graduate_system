from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student
from django.http import HttpResponse

def show(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    context = {"userinfo":uinfo}
    return render(request, 'student/setting/show.html',context)

# show student information   
def information(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    context = {"userinfo":uinfo}
    return render(request, 'student/setting/information.html',context)

#update student information
def infoupdate(request):
    try:
        id = request.session['studentuser']['sid']
        obj= student.objects.get(sid = id)
        obj.gender = request.POST['gender']
        obj.email = request.POST['email']
        obj.save()
        context = {"info": "Update Sucessful!","userinfo":obj,"status":1}
    except:
        context = {"info": "Update Failed!", "status":0, "view":"student_setting_information"}
    return render(request,"student/setting/info.html", context)


#edit password page
def password(request):
    id = request.session['studentuser']['sid']
    obj= student.objects.get(sid = id)
    context = {"userinfo":obj}
    return render(request,"student/setting/password.html", context)

#update password
def updatepwd(request):
    id = request.session['studentuser']['sid']
    obj= student.objects.get(sid = id)
    oldpassword = request.POST['oldpwd']

    if(oldpassword != obj.pw):
        context = {"info" : "Incorrect password!", "status":0, "view":"student_setting_password"}
    else:
        obj.pw = request.POST['newpwd']
        obj.save()
        context = {"info": "Update Sucessful!","userinfo":obj,"status":1}
    return render(request,"student/setting/info.html", context)