from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student, stuCourse, schedules, instructor, stuMsg, gradApplication
from django.http import HttpResponse
from datetime import datetime

def index(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    context = {"userinfo":uinfo}
    return render(request, 'student/AcademicRecord/index.html',context)

def stuHistory(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    stuRecord = stuCourse.objects.all().filter(sid = id).order_by("year","curStatus")

    data=[]
    for record in stuRecord:
        snum = record.sectionNum
        course = schedules.objects.get(sectionNum = snum )
        ins = instructor.objects.get(iid = course.iid)

        if record.curStatus == 2:
            status = "In progress"
        elif record.curStatus == 1:
            status = "Passed"
        elif record.curStatus == 3:
            status = "Grade is not assigned"
        else:
            status = "Failed"

        rlist = {"cid":record.cid, "className":course.className, "year":record.year, "semester":record.semester,
            "insName":ins.insName, "grade":record.grade, "curStatus":status}

        data.append(rlist)
    
    context = {"userinfo":uinfo, "data":data}
    return render(request, 'student/AcademicRecord/history.html',context)

def stugraduate(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    currentTaking = uinfo.class_taking
    passed = stuCourse.objects.all().filter(sid = id, curStatus = 1).count()
    failed = stuCourse.objects.all().filter(sid = id, curStatus = 0).count()
    taken = uinfo.class_taken
    context = {"userinfo":uinfo, "taken":taken, "current":currentTaking, "passed":passed}

    return render(request, 'student/AcademicRecord/stugraduate.html',context)

def applyGraudate(request):
    return HttpResponse ('<script>alert("Apply for Graduation?"); location.href = "submit";</script>')

def submitGradate(request):
    id = request.session['studentuser']['sid']
    uinfo= student.objects.get(sid = id)

    currentTaking = stuCourse.objects.all().filter(sid = id, curStatus = 2).count()
    passed = stuCourse.objects.all().filter(sid = id, curStatus = 1).count()

    gradObj = gradApplication.objects.filter(sid = id, curStatus = 0)

    if(gradObj.count() > 0):
        context = {"info": "You already submitted a graduate application! You cannot submit again. Please wait for registar to review your previous application.", "userinfo":uinfo}
        return render(request,"student/AcademicRecord/info.html", context)

    grad = gradApplication()
    grad.sid = id
    grad.ctaking = currentTaking
    grad.cpass = passed
    grad.save()

    notification = stuMsg()
    notification.receiverID = id
    notification.sender = "System"
    notification.title = "Graduate Application Submitted"
    
    notification.content = "You applied for graduated at " + str(datetime.now().strftime('%Y-%m-%d %H:%M')) +". Please wait for registar to review your application"
    notification.save()

    context = {"info": "Graudate Application Submitted !!  Registar will review your application in few days", "userinfo":uinfo}
    return render(request,"student/AcademicRecord/info.html", context)

