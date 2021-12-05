from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import course, period, schedules, review, stuCourse, stuMsg, insMsg, student, instructor

#view complain table page
def viewPeriod(request):
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    context = {"cur":cur, "uc":uc}
    return render(request, "myadmin/period/viewperiod.html", context)

def nextPeriod(request):
    # get the current term
    currentTerm = period.objects.get(curStatus = 2)
    x = currentTerm.term.split()
    Cyear= x[0]
    Csemester= x[1]

    sList = schedules.objects.filter(year = Cyear, semester = Csemester)
    rList = review.objects.all()
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    if cur.curPeriod == 5:
        return render(request, "myadmin/info.html", {"info" : "It is the last period of the term. You can only end the term!"})
    cur.curPeriod += 1
    if cur.curPeriod == 4:
        uc.curPeriod = 1
        for s in sList:
            s.status = "Closed"
            s.save()
    if cur.curPeriod == 5:
        uc.curPeriod = 2
        numCnt = dict()
        sumRate = dict()
        for r in rList:
            if r.sectionNum in numCnt:
                numCnt[r.sectionNum] = numCnt[r.sectionNum] + 1
                sumRate[r.sectionNum] = sumRate[r.sectionNum] + r.rating
            else:
                numCnt[r.sectionNum] = 1
                sumRate[r.sectionNum] = r.rating
        for sNum, cnt in numCnt.items():
            curRate = sumRate[sNum] / cnt
            curCourse = schedules.objects.get(sectionNum = sNum)
            curCourse.rating = curRate
            if curRate < 2:
                curInsMsg = insMsg()
                curInsMsg.receiverID = curCourse.iid
                curInsMsg.getTime = datetime.now()
                curIns = instructor.objects.get(iid = curCourse.iid)
                curIns.cp_num = curIns.cp_num + 1
                if curIns.cp_num == 3:
                    curIns.cp_num = 0
                    curInsMsg.title = "Suspend Notification"
                    curInsMsg.content = "You have 3 warnings and are now suspended, please contact the register office! "
                else:
                    curInsMsg.title = "Warning Notification"
                    curInsMsg.content = "You have a class that has a average rating below 2, and you received one warning! "
                curInsMsg.save()
            curCourse.save()
    cur.save()
    uc.save()
    #Send notifications to students and instructors that the period of the current semester has changed
    SENDER, TITLE = "register", "Period Changed"
    CONTENT = "Please be awared that the current period has changed!"
    stuList = student.objects.all()
    insList = instructor.objects.all()
    for s in stuList:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = s.sid
        curStuMsg.sender = SENDER
        curStuMsg.title = TITLE
        curStuMsg.content = CONTENT
        curStuMsg.getTime = datetime.now()
        curStuMsg.save()
    for i in insList:
        curInsMsg = insMsg()
        curInsMsg.receiverID = i.iid
        curInsMsg.title = TITLE
        curInsMsg.content = CONTENT
        curInsMsg.getTime = datetime.now()
        curInsMsg.save()
    return render(request, "myadmin/info.html", {"info" : "Successfully updated the period!"})

def endPeriod(request):
    stuList = student.objects.all()
    insList = instructor.objects.all()
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    if cur.curPeriod != 5:
        return render(request, "myadmin/info.html", {"info" : "You cannot end the term before having a grading period!"})
    cur.curStatus = -1
    uc.curStatus = 2
    nextTerm = period.objects.get(pid = uc.pid + 1)
    nextTerm.curStatus = 1
    cur.save()
    uc.save()
    nextTerm.save()
    
    #grading
    stuCourseList = stuCourse.objects.all()
    for sc in stuCourseList:
        if sc.curStatus == 2:
            if sc.grade is None:
                curSec = schedules.objects.get(sectionNum = sc.sectionNum)
                curIns = instructor.objects.get(iid = curSec.iid)
                curIns.cp_num = curIns.cp_num + 1
                if curIns.cp_num == 3:
                    curIns.curStatus = 0
                    curIns.cp_num = 0
                curIns.save()
            elif sc.grade != 'F':
                sc.curStatus = 1
                curStu = student.objects.get(sid = sc.sid)
                curSum = curStu.GPA * (float)(curStu.class_taken)
                curStu.class_taken = curStu.class_taken + 1
                if sc.grade == 'A':
                    curSum = curSum + 4.0
                elif sc.grade == 'B':
                    curSum = curSum + 3.0
                elif sc.grade == 'C':
                    curSum = curSum + 2.0
                else:
                    curSum = curSum + 1.0
                curStu.GPA = curSum / curStu.class_taken
                curStu.save()
            else:
                sc.curStatus = 0
                curCourse = course.objects.get(className = sc.className)
                curFailList = stuCourse.objects.filter(cid = curCourse.cid)
                if len(curFailList) > 1:
                    curStu = student.objects.get(sid = sc.sid)
                    curStu.curStatus = 0
                    curStu.save()                
            sc.save()
            
    #after grading, check students GPA
    for s in stuList:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = s.sid
        curStuMsg.sender = "register"
        curStuMsg.getTime = datetime.now()
        if s.GPA < 2:
            s.curStatus = 0
            curStuMsg.title = "Suspend Notification"
            curStuMsg.content = "You have been suspended because your GPA has dropped below 2.0"
            curStuMsg.save()
        elif s.GPA < 2.25:
            s.cp_num = s.cp_num + 1
            if s.cp_num == 3:
                s.cp_num = 0
                s.curStatus = 0
                curStuMsg.title = "Suspend Notification"
                curStuMsg.content = "You have been suspended because you have received 3 warnings!"
            else:
                curStuMsg.title = "Warning Notification"
                curStuMsg.content = "You have been warned because your GPA has dropped below 2.25"
            curStuMsg.save()
        elif s.GPA >= 3.75 and s.class_taken >= 4:
            if s.cp_num > 1: 
                s.cp_num = s.cp_num - 1
            curStuMsg.title = "Honor Notification"
            curStuMsg.content = "You have been chosen to be in the honor student lists, a warning will be removed if you currently have any warning records!"
            curStuMsg.save()
        s.save()
    
    #checking course GPA for instructors
    cntGPA = dict()
    sumGPA = dict()
    for sc in stuCourseList:
        if sc.sectionNum in sumGPA:
            cntGPA[sc.sectionNum] = cntGPA[sc.sectionNum] + 1
            if sc.grade is None:
                pass
            elif sc.grade == 'A':
                sumGPA[sc.sectionNum] = sumGPA[sc.sectionNum] + 4
            elif sc.grade == 'B':
                sumGPA[sc.sectionNum] = sumGPA[sc.sectionNum] + 3
            elif sc.grade == 'C':
                sumGPA[sc.sectionNum] = sumGPA[sc.sectionNum] + 2
            elif sc.grade == 'D':
                sumGPA[sc.sectionNum] = sumGPA[sc.sectionNum] + 1
        else:
            cntGPA[sc.sectionNum] =  1
            if sc.grade is None:
                sumGPA[sc.sectionNum] = 0
            elif sc.grade == 'A':
                sumGPA[sc.sectionNum] = 4
            elif sc.grade == 'B':
                sumGPA[sc.sectionNum] = 3
            elif sc.grade == 'C':
                sumGPA[sc.sectionNum] = 2
            elif sc.grade == 'D':
                sumGPA[sc.sectionNum] = 1
            else:
                sumGPA[sc.sectionNum] = 0
    for secNum, cntNum in cntGPA.items():
        currentGPA = sumGPA[secNum] / cntNum
        if currentGPA > 3.5 or currentGPA < 2.5:
            curSC = schedules.objects.get(sectionNum = secNum)
            curInsMsg = insMsg()
            curInsMsg.receiverID = curSC.iid
            curInsMsg.title = "Question regarding overall GPA"
            curInsMsg.content = "You have a class has an overall GPA obove 3.5 or below 2.5, please contact the register for a justification."
            curInsMsg.getTime = datetime.now()
            curInsMsg.save()
    
    #sending a notification to the students and instructors that the administrator has ended the period
    SENDER, TITLE = "register", "Term End"
    CONTENT = "The current term has ended. The next term is: " + nextTerm.term
    for s in stuList:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = s.sid
        curStuMsg.sender = SENDER
        curStuMsg.title = TITLE
        curStuMsg.content = CONTENT
        curStuMsg.getTime = datetime.now()
        curStuMsg.save()
    for i in insList:
        curInsMsg = insMsg()
        curInsMsg.receiverID = i.iid
        curInsMsg.title = TITLE
        curInsMsg.content = CONTENT
        curInsMsg.getTime = datetime.now()
        curInsMsg.save()
    return render(request, "myadmin/info.html", {"info" : "Successfully ended term!"})