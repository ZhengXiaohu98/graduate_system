from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from myadmin.models import student, stuCourse, schedules, instructor, period, stuMsg, payFine


def index(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # get the current term
    currentTerm = period.objects.get(curStatus = 2)
    upcoming = period.objects.get(curStatus = 1)
    x = currentTerm.term.split()
    Cyear= x[0]
    Csemester= x[1]
    y = upcoming.term.split()
    Nyear= y[0]
    Nsemester= y[1]

    # get the current taking courses
    Ccourse = stuCourse.objects.filter(sid = id ,curStatus = 2,year = Cyear, semester= Csemester)
    Dcourse = stuCourse.objects.filter(sid = id ,curStatus = 2,year = Cyear, semester= Csemester, grade = 'W')
    Ncourse = stuCourse.objects.filter(sid = id ,curStatus = 2,year = Nyear, semester = Nsemester)

    if(Ccourse.count() - Dcourse.count() + Ncourse.count() == 0):
        info1 = "! ! There is no current taking courses ! !"
        info2 = "! ! You did not add any course for next Semester ! !"
        data1 = 0
        data2 = 0
    elif(Ccourse.count() == 0):
        info1 = "! ! There is no current taking courses ! !"
        info2 = 0
        data2 = []
        data1 = 0
        for i in Ncourse:
            schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
            ins = instructor.objects.get(iid = schedulesObj.iid)
            rlist ={"year":i.year, "semester":i.semester, "cid":i.cid ,"className":schedulesObj.className, "section":i.sectionNum, 
                        "insName":ins.insName, "day":schedulesObj.days, "time":schedulesObj.start_time}
            data2.append(rlist)

    elif(Ncourse.count() == 0):
        info1 = 0
        info2 = "! ! You did not add any course for next Semester ! !"
        data1 = []
        data2=0
        for i in Ccourse:
            if(i.grade == 'W'):
                continue
            schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
            ins = instructor.objects.get(iid = schedulesObj.iid)
            rlist ={"year":i.year, "semester":i.semester, "cid":i.cid ,"className":schedulesObj.className, "section":i.sectionNum, 
                        "insName":ins.insName, "day":schedulesObj.days, "time":schedulesObj.start_time}
            data1.append(rlist)

    else:
        # get the current course inforation from schedule table
        info1 = 0
        info2 = 0
        data1=[]
        for i in Ccourse:
            schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
            ins = instructor.objects.get(iid = schedulesObj.iid)
            rlist ={"year":i.year, "semester":i.semester, "cid":i.cid ,"className":schedulesObj.className, "section":i.sectionNum, 
                        "insName":ins.insName, "day":schedulesObj.days, "time":schedulesObj.start_time}
            data1.append(rlist)

        # get the added courses for next term
        data2=[]
        for i in Ncourse:
            schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
            ins = instructor.objects.get(iid = schedulesObj.iid)
            rlist ={"year":i.year, "semester":i.semester, "cid":i.cid ,"className":schedulesObj.className, "section":i.sectionNum, 
                        "insName":ins.insName, "day":schedulesObj.days, "time":schedulesObj.start_time}
            data2.append(rlist)


    context = {"userinfo":uinfo, "info1":info1, "info2":info2, "Cterm": currentTerm.term,"Nterm":upcoming.term,
        "Ccourse":data1, "Ncourse":data2,"Ctake":Ccourse.count(), "Ntake":Ncourse.count(),
        "Cperiod":currentTerm.curPeriod, "Nperiod":upcoming.curPeriod}
    return render(request, 'student/CourseManagement/course.html',context)

def confirmdrop(request, section):
    scheduleObj = schedules.objects.get(sectionNum = section)

    Cperiod = period.objects.get(curStatus = 2)
    if( Cperiod.curPeriod == 4):
        info = "Drop " + scheduleObj.className + " (section#" + str(section) + ") ? You will recieve a grade W"
    else:
        info = "Drop " + scheduleObj.className + " (section#" + str(section) + ") ?"
    show = '<script>alert("%s"); location.href = "drop/%d";</script>'%(info,section)
    return HttpResponse (show)

def drop(request,section):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    scheduleObj = schedules.objects.get(sectionNum = section)

    #get current period
    Cperiod = period.objects.get(curStatus = 2)

    # not in registeration period => give grade W
    if (Cperiod. curPeriod == 4):
        Gcourse = stuCourse.objects.get(sid = id, sectionNum = section, curStatus = 2)
        Gcourse.grade = 'W'
        G.curStatus = 0
        Gcourse.save()

        # check if student dropped all courses, => suspended student
        Scourse = stuCourse.objects.filter(sid = id, curStatus = 2).count()
        Dcourse = stuCourse.objects.filter(sid = id, curStatus = 2, grade = 'W').count()
        if(Scourse-Dcourse == 0):
            notification = stuMsg()
            notification.receiverID = id
            notification.sender = "System"
            notification.title = "Current Status Changed"
            notification.content = "You dropped all courses for this semester. Your current status become SUSPENDED!!"
            notification.save()

            #change the status
            uinfo.curStatus = 0
            uinfo.save()

            # add fine to student account
            Ufine = payFine()
            Ufine.sid = id
            Ufine.save()

            info = "Class " + scheduleObj.className + " (section#" + str(section) + ") DROPPED! You recieved a grade W. Your current status will be: SUSPENDED"
        else:
            info = "Class " + scheduleObj.className + " (section#" + str(section) + ") DROPPED! You recieved a grade W"
    else: 
        Rcourse = stuCourse.objects.get(sid = id, sectionNum = section, curStatus = 2 )
        Rcourse.delete()

        # check if student dropped all courses, => suspended student
        Scourse = stuCourse.objects.filter(sid = id, curStatus = 2).count()
        Dcourse = stuCourse.objects.filter(sid = id, curStatus = 2, grade = 'W').count()
        if(Scourse-Dcourse == 0):
            notification = stuMsg()
            notification.receiverID = id
            notification.sender = "System"
            notification.title = "Current Status Changed"
            notification.content = "You dropped all courses for this semester. Your current status become SUSPENDED!!"
            notification.save()

            #change the status
            uinfo.curStatus = 0
            uinfo.save()

            # add fine to student account
            Ufine = payFine()
            Ufine.sid = id
            Ufine.save()

            info = "Class " + scheduleObj.className + " (section#" + str(section) + ") DROPPED! Your current status will be : SUSPENDED"
        else:
            info = "Class " + scheduleObj.className + " (section#" + str(section) + ") DROPPED!"

    context = {"userinfo":uinfo, "info":info}
    return render(request, 'student/CourseManagement/info.html',context)