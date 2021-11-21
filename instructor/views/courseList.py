from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication, schedules, stuCourse, student

#display the course for this instructor
def viewCourse(request):
    name = request.session['instructoruser']['insName']
    id = request.session['instructoruser']['iid']
    courses = schedules.objects.all().filter(iid = id).order_by("-current_enroll")
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
    context = {"students":data,"sectionNum":sectionNum, "className":course.className, "name":insname}
    return render(request, "instructor/courseList/stuInCourse.html",context)


def gradeUpdate(request,sectionNum=0):
    id = request.POST.get('sid')
    print(id)
    obj = stuCourse.objects.get(sectionNum = sectionNum, sid = id) #get obj in stuCourse
    print(obj.grade)
    print(obj.sectionNum)
    obj.grade = request.POST.get('grade') # change grade of the object
    # obj.save() #save change
    print(obj.grade)
    name = request.session['instructoruser']['insName']
    context = {"name":name}
    return render(request, "instructor/courseList/gradeInfo.html", context)