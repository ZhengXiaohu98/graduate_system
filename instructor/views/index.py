from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication,schedules,period,justification

#instructor index page
def index(request):
    name = request.session['instructoruser']['insName']
    id = request.session['instructoruser']['iid']
    courses = schedules.objects.all().filter(iid = id, status="open").order_by("-current_enroll")
    #current number of courses teaching
    numCourses = schedules.objects.all().filter(iid = id, status="open").count()
    #data is a list of course object currently teaching
    data = []
    for course in courses:
        sectionNum = course.sectionNum
        obj = schedules.objects.get(sectionNum=sectionNum)
        clist = {"sectionNum":obj.sectionNum,"className":obj.className, "year":obj.year, "current_enroll":obj.current_enroll,
                    "wait_list":obj.wait_list, "status":obj.status, "rating":obj.rating}
        data.append(clist)

    #Get current term and period
    periodObj = period.objects.get(curStatus = 2)
    term = periodObj.term
    periodDict = {0:"waiting", 1:"set-up", 2:"class register", 3:"special register", 4:"class running", 5:"grading"}
    curPeriod = periodDict[periodObj.curPeriod]

    #Get current status
    insObj = instructor.objects.get(iid = id)
    statusDict = {0:"Suspended", 1:"Normal"}
    curStatus = statusDict[insObj.curStatus]


    context = {"course" : data, "name":name, "numCourses":numCourses, "term":term,
                "curPeriod":curPeriod, "curStatus":curStatus}
    return render(request, 'instructor/index.html',context)

def sendJustification(request):
    
    name = request.session['instructoruser']['insName']
    id = request.session['instructoruser']['iid']
    justificationMsg = request.POST.get("justification")
    jusObj = justification()
    jusObj.content = justificationMsg
    jusObj.iid = id
    jusObj.curStatus = 0
    jusObj.save()

    context = {"name":name, "info":"Justification Submitted!"}
    return render(request, 'instructor/justificationInfo.html',context)
    
        # name = request.session['instructoruser']['insName']
        # context = {"name":name, "info":"Justification Failed!"}
        # return render(request, 'instructor/justificationInfo.html',context)
    

