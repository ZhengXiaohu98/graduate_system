from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication, schedules, stuCourse, student,waitList,course, period

#display the course for this instructor
def viewCourse(request):
    name = request.session['instructoruser']['insName']
    id = request.session['instructoruser']['iid']
    courses = schedules.objects.all().filter(iid = id).order_by("-status")
    data = []
    for course in courses:
        sectionNum = course.sectionNum
        obj = schedules.objects.get(sectionNum=sectionNum)
        clist = {"sectionNum":obj.sectionNum,"className":obj.className, "year":obj.year, "current_enroll":obj.current_enroll,
                    "wait_list":obj.wait_list, "status":obj.status, "rating":obj.rating}
        data.append(clist)

    context = {"course" : data, "name":name}
    return render(request, "instructor/courseList/courseList.html", context)

#display the students in this course
def stuInCourse(request,sectionNum=0):
    insname = request.session['instructoruser']['insName']
    #get current period
    curPeriod = period.objects.get(curStatus=2).curPeriod
    #get students
    students = stuCourse.objects.all().filter(sectionNum = sectionNum).order_by("sid")
    stuNum = stuCourse.objects.all().filter(sectionNum = sectionNum).count()
    course = schedules.objects.get(sectionNum=sectionNum)
    course.current_enroll = stuNum
    course.save()
    data = []
    for s in students:
        studentid = s.sid
        obj = stuCourse.objects.get(sid=studentid,sectionNum=sectionNum)
        stu = student.objects.get(sid=studentid)
        name = stu.stuName
        slist = {
            "sid":obj.sid, "year":obj.year, "semester":obj.semester, 
            "grade":obj.grade,"curStatus":obj.curStatus, "name":name,
        }
        
        data.append(slist)
    context = {"students":data,"sectionNum":sectionNum, "className":course.className, "name":insname,"curPeriod":curPeriod}
    return render(request, "instructor/courseList/stuInCourse.html",context)


def gradeUpdate(request,sectionNum=0):
    id = request.POST.get('sid')
    grade = request.POST.get('grade')
    name = request.session['instructoruser']['insName']
    stuCourseObj = stuCourse.objects.get(sectionNum = sectionNum, sid = id) #get obj in stuCourse

    # change grade of the object
    stuCourseObj.grade = grade 
    stuCourseObj.save()

    context = {"name":name,"sectionNum":sectionNum,"info":"Update Successfully"}
    return render(request, "instructor/courseList/gradeInfo.html", context)


def viewWaitlist(request,sectionNum=0):
    name = request.session['instructoruser']['insName']
    waitlistQuery = waitList.objects.all().filter(sectionNum = sectionNum).order_by("position")
    data = []
    for waitingObj in waitlistQuery:
        position = waitingObj.position
        obj = waitList.objects.get(position=position)
        stuName = student.objects.get(sid = obj.sid).stuName
        wlist = {"sectionNum":obj.sectionNum,"sid":obj.sid, "year":obj.year,
                    "position":position, "semester":obj.semester, "stuName":stuName}
        data.append(wlist)
    context = {"name":name, "waitlist":data, "sectionNum":sectionNum}
    return render(request, "instructor/courseList/waitlist.html", context)


def waitlistUpdate(request,sid=0):
    name = request.session['instructoruser']['insName']
    
    #gather info we need
    waitlistObj = waitList.objects.get(sid=sid)
    sectionNum = waitlistObj.sectionNum
    position = waitlistObj.position
    try:    
        #need things like course name to stuCourse obj
        scheduleObj = schedules.objects.get(sectionNum=sectionNum)
        scheduleObj.wait_list -= 1
        scheduleObj.current_enroll += 1
        scheduleObj.save()
        className = scheduleObj.className
        
        courseObj = course.objects.get(className = className)
        cid = courseObj.cid
        #create new stuCourse Obj so I can add the student to the course
        stuCourseObj = stuCourse()
        stuCourseObj.sid = sid
        stuCourseObj.cid = cid
        stuCourseObj.sectionNum = sectionNum
        stuCourseObj.year = scheduleObj.year
        stuCourseObj.semester = scheduleObj.semester
        stuCourseObj.grade = None
        stuCourseObj.curStatus = 2
        stuCourseObj.save()

        #now need to handle the waitlist
        
        #decrease other greater position waitlist obj by 1
        waitlistQuery = waitList.objects.all().filter(sectionNum = sectionNum).order_by("position")
        for greaterObj in waitlistQuery:
            if greaterObj.position > position:
                print(f"Before: sid:{greaterObj.sid}  position:{greaterObj.position}")
                greaterObj.position = greaterObj.position - 1
                print(f"After: sid:{greaterObj.sid}  position:{greaterObj.position}")
                greaterObj.save()
        
        #delete current waitlist obj 
        waitlistObj.delete()
        
        context = {"name":name, "sectionNum":sectionNum, "info":f"Added Student to section {sectionNum} Successfully!"}
        return render(request, "instructor/courseList/waitlistInfo.html", context)
    except:
        context = {"name":name, "sectionNum":sectionNum, "info":f"Failed to add Student to section {sectionNum}!"}
        return render(request, "instructor/courseList/waitlistInfo.html", context)