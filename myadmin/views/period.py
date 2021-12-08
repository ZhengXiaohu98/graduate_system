from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import course, period, schedules, review, stuCourse, stuMsg, insMsg, student, instructor, payFine

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
    stuList = student.objects.all()
    if cur.curPeriod == 3:
        for s in sList:
            if s.current_enroll < 5:
                s.status = "Cancel"
                s.save()
                curInsMsg = insMsg()
                curInsMsg.receiverID = s.iid
                curInsMsg.title = "Class Canceled"
                curInsMsg.content = s.className + " have been canceled because less than 5 student enrolled."
                curInsMsg.save()
                # check if a instrutor  whose courses were all canceled
                Origin = sList.filter(iid = s.iid).count()
                Cancel = sList.filter(iid = s.iid, status = "Cancel").count()
                if Origin - Cancel == 0 :
                    curInsMsg = insMsg()
                    curInsMsg.receiverID = s.iid
                    curInsMsg.title = "Your Current Status"
                    curInsMsg.content = "All courses in your teaching list have been canceled. You current become SUSPENDED !"
                    curInsMsg.save()
                    ins = instructor.objects.get(iid = s.iid)
                    ins.curStatus = 0
                    ins.save()
                # get the student who added cancelled class
                stuCourseObj = stuCourse.objects.filter(sectionNum = s.sectionNum)
                for sc in stuCourseObj:
                    curStuMsg = stuMsg()
                    curStuMsg.receiverID = sc.sid
                    curStuMsg.sender = "Registar"
                    curStuMsg.title = "Class Canceled"
                    curStuMsg.content = s.className + " have been canceled and removed from your schedule."
                    curStuMsg.save()
                    sc.delete()
                    stu = stuList.get(sid = sc.sid)
                    stu.class_taking -= 1
                    stu.save()

        # check student who has less than 2 courses
        stuObj = stuList.filter(curStatus = 1)
        for s in stuObj:
            scObj = stuCourse.objects.filter(sid = s.sid, year = Cyear, semester =Csemester)
            if scObj.count() == 1:
                curStuMsg = stuMsg()
                curStuMsg.receiverID = s.sid
                curStuMsg.sender = "Registar"
                curStuMsg.title = "Need to Enroll More Classes"
                curStuMsg.content = "You must enroll at least 2 classes. Enroll more class please"
                curStuMsg.save()    

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
    SENDER, TITLE = "Registar", "Period Changed"
    CONTENT = "Please be awared that the current period has changed!"
    stuList = student.objects.all()
    insList = instructor.objects.all()
    for s in stuList:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = s.sid
        curStuMsg.sender = SENDER
        curStuMsg.title = TITLE
        curStuMsg.content = CONTENT
        curStuMsg.save()
    for i in insList:
        curInsMsg = insMsg()
        curInsMsg.receiverID = i.iid
        curInsMsg.title = TITLE
        curInsMsg.content = CONTENT
        curInsMsg.save()
    return render(request, "myadmin/info.html", {"info" : "Successfully updated the period!"})

def endPeriod(request):
    stuList = student.objects.all()
    insList = instructor.objects.all()
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    if cur.curPeriod != 5:
        return render(request, "myadmin/info.html", {"info" : "You cannot end the term before having a grading period!"})
    
    x = cur.term.split()
    Cyear= x[0]
    Csemester= x[1]

    #grading
    scList = stuCourse.objects.filter(curStatus = 2, year = Cyear, semester = Csemester)
    for sc in scList:
        curStu = student.objects.get(sid = sc.sid)
        if sc.grade is None:
            sc.curStatus = 3
            curSec = schedules.objects.get(sectionNum = sc.sectionNum)
            curIns = instructor.objects.get(iid = curSec.iid)
            curIns.cp_num = curIns.cp_num + 1
            curInsMsg = insMsg()
            curInsMsg.receiverID = curIns.iid
            curInsMsg.title = "Grade Missing"              
            if curIns.cp_num == 3:
                curIns.curStatus = 0
                curIns.cp_num = 0
                curInsMsg.content = "You must assign grade for all students. You have been warned due to the grade missing. You currenly have 3 warning, your status changed to SUSPENDED!"
            curIns.save()
            curInsMsg.content = "Grade missing for student : " + curStu.stuName + ". You have been warned due to the grade missing."
            curInsMsg.save()     
        elif sc.grade != 'F':
            sc.curStatus = 1
            curSum = curStu.GPA * (float)(curStu.class_taken)
            if sc.grade == 'A':
                curSum = curSum + 4.0
            elif sc.grade == 'B':
                curSum = curSum + 3.0
            elif sc.grade == 'C':
                curSum = curSum + 2.0
            else:
                curSum = curSum + 1.0
            curStu.GPA = curSum / curStu.class_taken
        else:
            sc.curStatus = 0
            curCourse = course.objects.get(className = sc.className)

            #check if a student fail a same course two time
            pastObj = stuCourse.objects.filter(cid = sc.cid, sid = sc.sid, grade='F')
            if pastObj.count() >= 1 :
                stuObj = student.objects.get(sid = id)
                stuObj.curStatus  = 0
                stuObj.save()

                courseObj = course.objects.get(cid = sc.cid)
                curStuMsg = stuMsg()
                curStuMsg.receiverID = sc.sid
                curStuMsg.sender = "register"
                curStuMsg.title = "Suspended Notification"
                curStuMsg.content = "You have been failed " + courseObj.className +" twice. Your current SUSPENDED"
                curStuMsg.save()

                # add fine to student account
                Ufine = payFine()
                Ufine.sid = sc.sid
                Ufine.save()

        curStu.class_taken += 1
        curStu.class_taking -= 1            
        sc.save()
        curStu.save()

    #check student semester GPA 
    for stu in stuList:
        stuSemCourse = stuCourse.objects.filter(year = Cyear, semester = Csemester, sid = stu.sid)
        if stuSemCourse.count() > 0:
            curSum = 0
            count = 0
            for sc in stuSemCourse:
                if sc.grade == 'A':
                    curSum = curSum + 4.0
                elif sc.grade == 'B':
                    curSum = curSum + 3.0
                elif sc.grade == 'C':
                    curSum = curSum + 2.0
                elif sc.grade == 'D':
                    curSum = curSum + 1.0
                else:
                    curSum = curSum + 0.0
                count += 1.0
            
            gpa = curSum / count
            if gpa > 3.75:
                if stu.cp_num > 1: 
                    stu.cp_num = stu.cp_num - 1
                curStuMsg = stuMsg()
                curStuMsg.receiverID = stu.sid
                curStuMsg.sender = "register"
                curStuMsg.title = "Honor Notification"
                curStuMsg.content = "You have been chosen to be in the honor student lists, a warning will be removed if you currently have any warning records!"
                curStuMsg.save()


    #after grading, check students GPA
    for s in stuList:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = s.sid
        curStuMsg.sender = "register"
        if s.GPA < 2:
            s.curStatus = 0
            curStuMsg.title = "Suspend Notification"
            curStuMsg.content = "You have been suspended because your GPA has dropped below 2.0"
            curStuMsg.save()

            # add fine to student account
            Ufine = payFine()
            Ufine.sid = s.sid
            Ufine.save()

        elif s.GPA < 2.25:
            s.cp_num = s.cp_num + 1
            if s.cp_num == 3:
                s.cp_num = 0
                s.curStatus = 0
                curStuMsg.title = "Suspend Notification"
                curStuMsg.content = "You have been suspended because you have received 3 warnings!"

                # add fine to student account
                Ufine = payFine()
                Ufine.sid = s.sid
                Ufine.save()

            else:
                curStuMsg.title = "Warning Notification"
                curStuMsg.content = "You have been warned because your GPA has dropped below 2.25"
            curStuMsg.save()
        elif s.GPA >= 3.5:
            if s.cp_num > 1: 
                s.cp_num = s.cp_num - 1
            curStuMsg.title = "Honor Notification"
            curStuMsg.content = "You have been chosen to be in the honor student lists, a warning will be removed if you currently have any warning records!"
            curStuMsg.save()
        s.save()
    
    stuCourseList = stuCourse.objects.filter(semester = Csemester, year = Cyear)
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
        print(currentGPA)
        if currentGPA > 3.5 or currentGPA < 2.5:
            curSC = schedules.objects.get(sectionNum = secNum)
            curInsMsg = insMsg()
            curInsMsg.receiverID = curSC.iid
            curInsMsg.title = "Question regarding overall GPA"
            curInsMsg.content = "You have a class has an overall GPA obove 3.5 or below 2.5, please contact the register for a justification."
            curInsMsg.save()
    
    #end period
    cur.curStatus = -1
    uc.curStatus = 2
    nextTerm = period.objects.get(pid = uc.pid + 1)
    nextTerm.curStatus = 1
    cur.save()
    uc.save()
    nextTerm.save()

    #sending a notification to the students and instructors that the administrator has ended the period
    SENDER, TITLE = "register", "Term End"
    CONTENT = "The current term has ended. The next term is: " + nextTerm.term
    for s in stuList:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = s.sid
        curStuMsg.sender = SENDER
        curStuMsg.title = TITLE
        curStuMsg.content = CONTENT
        curStuMsg.save()
    for i in insList:
        curInsMsg = insMsg()
        curInsMsg.receiverID = i.iid
        curInsMsg.title = TITLE
        curInsMsg.content = CONTENT
        curInsMsg.save()
    return render(request, "myadmin/info.html", {"info" : "Successfully ended term!"})