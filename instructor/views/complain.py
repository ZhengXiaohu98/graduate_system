from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication, schedules, complainmsg, student, stuCourse
<<<<<<< HEAD

def editComplain(request):
    name = request.session['instructoruser']['insName']
    context = {"name":name}
=======
from django.core.paginator import Paginator
def editComplain(request,pIndex=1):
    name = request.session['instructoruser']['insName']
    id = request.session['instructoruser']['iid']
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
    
    #get complain history
    complainmsgObj = complainmsg.objects.filter(fromId=id)
    count = complainmsgObj.count()
    complain = []
    num = 1
    for i in complainmsgObj:
        if i.curStatus == 0:
            status = "pending"
        else:
            status = "processed"
        detail = {"num":num, "type":i.receiveType, "receiver":i.receiveName, 
                  "time":i.createdTime, "status":status}
        complain.append(detail)
        num+=1

    #seperate page when displaying complain history
    p = Paginator(complain, 10)
    if(pIndex<1):
        pIndex=1
    if(pIndex>p.num_pages):
        pIndex=p.num_pages
    complain1 = p.page(pIndex)

    if(count==0):
        context = {"name":name,  "studentName":stuName, "className":className, "history":"No complain history exist",
                "pIndex":pIndex, "pagelist":p.page_range, "check":0}

    context = {"name":name,  "studentName":stuName, "className":className, "complain":complain1,
                "pIndex":pIndex, "pagelist":p.page_range, "check":1}
>>>>>>> b5990fff3592c6072827bd6e368b8735286a81de
    return render(request,"instructor/complain/newComplain.html",context)


def updateComplain(request):
    name = request.session['instructoruser']['insName']
    try:
        id = request.session['instructoruser']['iid']
        ins = instructor.objects.get(iid=id)
<<<<<<< HEAD
        objname = request.POST.get("complainName")
=======
        objname = request.POST.get("name")
        objdiscription = request.POST.get("description")
>>>>>>> b5990fff3592c6072827bd6e368b8735286a81de
        obj = student.objects.get(stuName = objname)
        print(obj)
        complain = complainmsg()
        complain.sendType = "Instructor"
        complain.fromId = id
        complain.fromName = ins.insName
        complain.receiveType = "Student"
        complain.receiveId = obj.sid
        complain.receiveName = obj.stuName
<<<<<<< HEAD
=======
        complain.description = objdiscription
>>>>>>> b5990fff3592c6072827bd6e368b8735286a81de
        complain.save()
        context = {"info":"Complain Successfully!","name":name}
        return render(request,"instructor/complain/complainInfo.html",context)
    except:
        context = {"info":"Complain Failed! Make sure student name exists!","name":name}
        return render(request,"instructor/complain/complainInfo.html",context)