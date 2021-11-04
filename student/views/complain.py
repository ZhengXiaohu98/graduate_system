from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student, stuApplication, stuCourse, instructor, schedules, complainmsg
from django.http import HttpResponse
from django.core.paginator import Paginator


def stuComplain(request):
    return redirect(reverse('complain_student' , args = (0,0,0,1, )))

def stuComplainStu(request, info, name, description, pIndex = 1):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    
    #get the current taking courses
    course = stuCourse.objects.filter(sid = id, curStatus = 2)
    data = []
    names = []

    #get the class name of current taking courses
    for i in course:
        schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)

        x = schedulesObj.className.split()
        cName = ""
        for element in x:
            cName += element

        rlist = {"label":cName, "cid":i.cid}
        data.append(rlist)

        # get students name from curren taking course
        stuCourseObj = stuCourse.objects.filter(sectionNum = i.sectionNum).exclude(sid = id)

        for stu in stuCourseObj:
            studentObj = student.objects.get(sid = stu.sid)
            stuinfo = {"cid":i.cid, "names":studentObj.stuName}
            names.append(stuinfo)


    # get the complain history
    complainmsgObj = complainmsg.objects.filter(fromId = id)
    count = complainmsgObj.count()
    
    complain = []
    num = 1
    for j in complainmsgObj:
        if j.curStatus == 0:
            status = "pending"
        else:
            status = "processed"
        detail = {"num":num, "type":j.receiveType , "receiver":j.receiveName, "time":j.createdTime, "status":status}
        complain.append(detail)
        num += 1

    

    #seperate complain history into 10/per page
    p = Paginator(complain, 10) 
    if(pIndex < 1):
        pIndex = 1
    if(pIndex > p.num_pages):
        pIndex = p.num_pages

    complain1 = p.page(pIndex)

    if count == 0:
        context = {"userinfo":uinfo, "course":data,"studentName":names, "info":info, "name":name, "description":description, 
                    "historyinfo":"No Complain History Exist!", "pIndex":pIndex, "pagelist":p.page_range, "check":0}
        return render(request, 'student/complain/stuform.html', context) 

    context = {"userinfo":uinfo, "course":data,"studentName":names, "info":info, "name":name, "description":description, 
            "complain":complain1, "pIndex":pIndex, "pagelist":p.page_range, "check":1}
    return render(request, 'student/complain/stuform.html',context)

def stuComplainIns(request, info, name, description, pIndex = 1):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    
    course = stuCourse.objects.filter(sid = id, curStatus = 2)
    data = []
    for i in course:
        schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
        ins = instructor.objects.get(iid = schedulesObj.iid)
        rlist = {"insName":ins.insName}
        data.append(rlist)

    # get the complain history
    complainmsgObj = complainmsg.objects.filter(fromId = id)
    count = complainmsgObj.count()
    
    complain = []
    num = 1
    for j in complainmsgObj:
        if j.curStatus == 0:
            status = "pending"
        else:
            status = "processed"
        detail = {"num":num, "type":j.receiveType , "receiver":j.receiveName, "time":j.createdTime, "status":status}
        complain.append(detail)
        num += 1

    #seperate complain history into 10/per page
    p = Paginator(complain, 10) 
    if(pIndex < 1):
        pIndex = 1
    if(pIndex > p.num_pages):
        pIndex = p.num_pages

    complain1 = p.page(pIndex)

    if count == 0:
        context = {"userinfo":uinfo, "instructor":data, "info":info, "name":name, "description":description, 
                    "historyinfo":"No Complain History Exist!", "pIndex":pIndex, "pagelist":p.page_range, "check":0}
        return render(request, 'student/complain/insform.html', context) 

    context = {"userinfo":uinfo, "instructor":data, "info":info, "name":name, "description":description,
     "complain":complain1, "pIndex":pIndex, "pagelist":p.page_range, "check":1}
    return render(request, 'student/complain/insform.html',context)

def formSubmitStu(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    stu = request.POST['name']
    description = request.POST['description']

    if stu == "Choose Student Name" and description == "":
        info = "You must choose student name and write the description!!"
        description = 0
    elif stu == "Choose Student Name":
        info = "Choose student name please!!"
    elif description == "":
        info = "Description cannot be empty"
        description = 0
    else:
        stuObj = student.objects.get(stuName = stu)
        complain = complainmsg()
        complain.sendType = "student"
        complain.fromId = id
        complain.fromName = uinfo.stuName
        complain.receiveType = "Student"
        complain.receiveId = stuObj.sid
        complain.receiveName = stuObj.stuName
        complain.description = description
        complain.save()
        context = {"userinfo":uinfo, "info":"Complain submitted !! Please wait for registar to review!!"}
        return render(request, 'student/complain/info.html',context)

    return redirect(reverse('complain_student', args = (info, stu, description, 1,  )))

def formSubmitIns(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    ins = request.POST['name']
    description = request.POST['description']

    if ins == "Choose Instructor Name" and description == "":
        info = "You must choose instructor name and write the description!!"
        description = 0
    elif ins == "Choose Instructor Name":
        info = "Choose instructor name please!!"
    elif description == "":
        info = "Description cannot be empty"
        description = 0
    else:
        insObj = instructor.objects.get(insName = ins)
        complain = complainmsg()
        complain.sendType = "student"
        complain.fromId = id
        complain.fromName = uinfo.stuName
        complain.receiveType = "Instructor"
        complain.receiveId = insObj.iid
        complain.receiveName = insObj.insName
        complain.description = description
        complain.save()
        context = {"userinfo":uinfo, "info":"Complain submitted !! Please wait for registar to review!!"}
        return render(request, 'student/complain/info.html',context)

    return redirect(reverse('complain_instructor', args = (info, ins, description, 1, )))



