from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication, schedules, stuCourse, student, insMsg, stuMsg, period
from datetime import datetime
from django.core.paginator import Paginator 
def Notification(request, pIndex=1):
    id = request.session['instructoruser']['iid']
    name = request.session['instructoruser']['insName']
    notification = insMsg.objects.filter(receiverID = id).order_by('getTime').reverse()
    if (notification.count() == 0):
            notify = 0
    else:
        notify =[]
        for i in notification:
            if i.status == 0:
                show = "UNREAD"
            else:
                show = "READ"
            rlist = {"nid":i.nid, "time":i.getTime, "title": i.title, "content":i.content, "status":show}
            notify.append(rlist)

        p = Paginator(notify, 5) 

        if(pIndex < 1):
            pIndex = 1
        if(pIndex > p.num_pages):
            pIndex = p.num_pages

        notify = p.page(pIndex)

    stuName=[]
    className=[]

    #get section number by instructor id
    secNum = schedules.objects.filter(iid = id)
    
    
    for section in secNum:
        #get courses by section number
        courses = stuCourse.objects.filter(sectionNum = section.sectionNum, curStatus=2)
        
        for course in courses:

            scheduleObj = schedules.objects.get(sectionNum = course.sectionNum)
            x = scheduleObj.className.split()
            cName = ""
            for element in x:
                cName+=element
            
            rlist = {"label":cName}
            if rlist not in className:
                className.append(rlist)

            #get student by sid
            stu = student.objects.get(sid = course.sid)
            stuName.append(stu.stuName)


    context = {"notification":notify,"name":name,"studentName":stuName, "className":className}
    if(notify != 0):
        context["pIndex"] = pIndex
        context["pagelist"] = p.page_range

    return render(request,"instructor/notification/notification.html", context)

def sendNotification(request):
    try:
        id = request.session['instructoruser']['iid']
        name = request.session['instructoruser']['insName']
        ins = instructor.objects.get(iid=id)
        #getting information from POST
        objName = request.POST.get("name")
        objTitle = request.POST.get("title")
        objContent = request.POST.get("content")
        #get receiver id by student name
        stu = student.objects.get(stuName = objName)
        objReceiverId = stu.sid
        #create new stuMsg Object
        stuMsgObj = stuMsg()
        stuMsgObj.receiverID = objReceiverId
        stuMsgObj.sender = "Instructor"
        stuMsgObj.title = objTitle
        stuMsgObj.content = objContent
        #stuMsgObj.save()
        print(stuMsgObj)
        context = {"name":name,"info":"Notification Sent Succesfully!"}
        return render(request,"instructor/notification/notificationInfo.html", context)
    except:
        context = {"name":name,"info":"Notification Sent Failed!"}
        return render(request,"instructor/notification/notificationInfo.html", context)