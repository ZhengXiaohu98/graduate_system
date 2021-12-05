from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import gradApplication, student, stuMsg

#view graduate table page
def viewGraduate(request, pIndex=1):
    grdList = gradApplication.objects.all()
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(grdList, 10)
    maxPages = p.num_pages
    #check if exceed the page limit or invalid page index
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    # get the cur list
    retList = p.page(pIndex)
    #get the page range
    pRange = p.page_range
    context = {"grdlist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex}
    return render(request, "myadmin/graduate/viewgraduate.html", context)

def dealGraduateA(request, ggid):
    curGrd = gradApplication.objects.get(gid = ggid)
    curstu = student.objects.get(sid = curGrd.sid)
    curstu.curStatus = 2
    curstu.save()
    curGrd.curStatus = 1
    curGrd.save()

    notify = stuMsg()
    notify.receiverID = curGrd.sid
    notify.sender = Registar
    notify.title = "Graduate Application"
    notify.content = "Your graduate application has been approved!"
    notify.save()

    context = {"info" : "The student's graduate application has been approved!"}
    return render(request, "myadmin/info.html", context)

def dealGraduateR(request, ggid):
    curGrd = gradApplication.objects.get(gid = ggid)
    curGrd.curStatus = 2
    curGrd.save()

    stuObj = student.objects.get(sid = curGrd.sid)
    stuObj.cp_num += 1
    
    if(stuObj.cp_num >=3):
        stuObj.cp_num -= 3
        stuObj.curStatus = 0

    stuObj.save()

    notify = stuMsg()
    notify.receiverID = curGrd.sid
    notify.sender = "Registar"
    notify.title = "Graduate Application"
    notify.content = "Your graduate application has been rejected! You received a warning for reckless graduation application"
    notify.save()

    context = {"info" : "The student's graduate application has been rejected!"}
    return render(request, "myadmin/info.html", context)
