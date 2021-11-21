from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student, schedules, instructor, course
from django.http import HttpResponse
import pickle


def search(request, check):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    schedulesObj = schedules.objects.all()
    
    terms = schedules.objects.values_list('year', 'semester').distinct()
    terms.query = pickle.loads(pickle.dumps(terms.query))
    courses = course.objects.all()
    days = schedules.objects.values_list('days').distinct()
    days.query = pickle.loads(pickle.dumps(days.query))
    times = schedules.objects.values_list('start_time').distinct()
    times.query = pickle.loads(pickle.dumps(times.query))
    
    # combine year and semester => term
    dataterms = []
    for i in terms:
        term = str(i["year"]) + " " + i["semester"]
        dataterms.append(term)

    
    if check == 1:
        context = {"userinfo":uinfo, "course": courses, "term":dataterms,"time":times, "day":days, "check":1}
    else:
        context = {"userinfo":uinfo, "course": courses, "term":dataterms,"time":times, "day":days, "check":0}

    return render(request, 'student/SearchCourse/search.html',context)


def searchmodify(request, search):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    schedulesObj = schedules.objects.all()
  
    terms = schedules.objects.values_list('year', 'semester').distinct()
    terms.query = pickle.loads(pickle.dumps(terms.query))
    courses = course.objects.all()
    days = schedules.objects.values_list('days').distinct()
    days.query = pickle.loads(pickle.dumps(days.query))
    times = schedules.objects.values_list('start_time').distinct()
    times.query = pickle.loads(pickle.dumps(times.query))
    
    if search == 1:
        info = "You must select something to proceed"
        context = {"userinfo": uinfo, "info":info, "search":search}
        return render(request, 'student/SearchCourse/searchmodify.html',context)


    search = search.split(",")

    # combine year and semester => term
    dataterms = []
    for i in terms:
        term = str(i["year"]) + " " + i["semester"]
        dataterms.append(term)

    context = {"userinfo":uinfo, "course": courses, "term":dataterms,"time":times, "day":days, 
            "mterm":search[0],"mcourse":search[1],"mday":search[2],"mtime":search[3], "mstatus":search[4]}
    
    return render(request, 'student/SearchCourse/searchmodify.html',context)


def courses(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    term = request.POST['term']
    classname = request.POST['course']
    day = request.POST['day']
    time = request.POST['time']
    status = request.POST['status']
    search = term + "," + classname + "," + day + "," + time + ","+ status

    # search for the course
    if term == 'Choose Term' and classname == 'Choose Course' and day == "Choose Day" and time == "Choose Time" and status == "Choose Status":
        return redirect(reverse('student_SearchCourse', args = (1,)))

    schedulesObj = schedules.objects.all()

    if term != 'Choose Term' :
        x = term.split()
        year = x[0]
        semester = x[1]
        schedulesObj = schedulesObj.filter(year = year, semester = semester)

    if classname != 'Choose Course':
        schedulesObj =schedulesObj.filter(className = classname)
    if day != 'Choose Day':
        schedulesObj =schedulesObj.filter(days = day)
    if time != 'Choose Time':
        schedulesObj =schedulesObj.filter(start_time = time)
    if status != 'Choose Status':
        schedulesObj =schedulesObj.filter(status = status)

      

    count = schedulesObj.count()
    # in case there is no course result found
    if count ==0:
        info = "No result found! Try to modify your search!"
        context = {"userinfo": uinfo, "info":info, "search":search}
        return render(request, 'student/SearchCourse/info.html',context)

    print(schedulesObj)
    data=[]
    for obj in schedulesObj:
        insObj = instructor.objects.get(iid = obj.iid)
        courseObj = course.objects.get(className = obj.className)

        print(courseObj) 
        rlist = {"year":obj.year, "semester":obj.semester,"cid":courseObj.cid, "className":obj.className, 
            "section":obj.sectionNum,"insName":insObj.insName, "day":obj.days, "time":obj.start_time,"status":obj.status}

        data.append(rlist)

    context = {"userinfo":uinfo,"course": data, "search":search}
    return render(request, 'student/SearchCourse/courseslist.html',context)