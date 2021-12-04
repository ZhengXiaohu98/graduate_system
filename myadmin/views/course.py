from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import schedules, instructor, course

def viewCourse(request, pIndex=1):
    courseList = course.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        courseList = courseList.filter(Q(cid__contains=kw) | Q(className__contains=kw) | Q(department__contains=kw))
        myKey.append('keyword='+kw)
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(courseList, 10)
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

    context = {"courselist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey}
    return render(request, "myadmin/course/view_course.html", context)

def addCourse(request):
    insList = instructor.objects.all()
    return render(request, "myadmin/course/add_course.html", {"insList":insList})

def insertCourse(request):
    classname = request.POST["classname"]
    year = request.POST["year"]
    semester = request.POST["semester"]
    iid = request.POST["iid"]
    dept = request.POST["department"]
    nothing_checked = True
    days = ""
    mo = request.POST.get("mo", None)
    tu = request.POST.get("tu", None)
    we = request.POST.get("we", None)
    th = request.POST.get("th", None)
    fr = request.POST.get("fr", None)
    sa = request.POST.get("sa", None)
    if mo is not None:
        days = days + '&' + mo
        nothing_checked = False
    if tu is not None:
        days = days + '&' + tu
        nothing_checked = False
    if we is not None:
        days = days + '&' + we
        nothing_checked = False
    if th is not None:
        days = days + '&' + th
        nothing_checked = False
    if fr is not None:
        days = days + '&' + fr
        nothing_checked = False
    if sa is not None:
        days = days + '&' + sa
        nothing_checked = False
    if nothing_checked:
        return render(request, "myadmin/info.html", {"info" : "You didn't select any days for the course!"})
    days = days[1:]
    start_time = request.POST["start_time"]
    max_limit = request.POST["max_limit"]
    TIME = ""
    if start_time == 'a':
        TIME = "09:30 - 10:45"
    if start_time == 'b':
        TIME = "11:00 -12:15"
    if start_time == 'c':
        TIME = "11:00 -12:15"
    if start_time == 'd':
        TIME = "11:00 -12:15"
    #save the course in the database
    newSc = schedules()
    newSc.className = classname
    newSc.iid = (int)(iid)
    newSc.year = (int)(year)
    newSc.semester = semester
    newSc.days = days
    newSc.start_time = TIME
    newSc.max_limit = max_limit
    newSc.status = "open"
    newSc.rating = None
    newSc.save()
    context = {"info" : "Successfully added Course!"}
    
    newCourse = course()
    newCourse.className = classname
    newCourse.pre_req = 0
    newCourse.department = dept
    newCourse.save()
    
    return render(request, "myadmin/info.html", context)

def editCourse(request, cid):
    try:
        insList = instructor.objects.all()
        obj = course.objects.get(cid = cid)
        sc = schedules.objects.get(sectionNum = cid)
        context = {"course" : obj, "insList":insList, "sc" : sc}
        return render(request, "myadmin/course/edit_course.html", context)
    except:
        context = {"info" : "Error edit Course!"}
        return render(request, "myadmin/info.html", context)

def updateCourse(request):
    obj = course.objects.get(cid = request.POST['cid'])
    sch = schedules.objects.get(sectionNum = request.POST['cid'])
    obj.className = request.POST["classname"]
    obj.department = request.POST["department"]
    obj.save()
    nothing_checked = True
    days = ""
    mo = request.POST.get("mo", None)
    tu = request.POST.get("tu", None)
    we = request.POST.get("we", None)
    th = request.POST.get("th", None)
    fr = request.POST.get("fr", None)
    sa = request.POST.get("sa", None)
    if mo is not None:
        days = days + '&' + mo
        nothing_checked = False
    if tu is not None:
        days = days + '&' + tu
        nothing_checked = False
    if we is not None:
        days = days + '&' + we
        nothing_checked = False
    if th is not None:
        days = days + '&' + th
        nothing_checked = False
    if fr is not None:
        days = days + '&' + fr
        nothing_checked = False
    if sa is not None:
        days = days + '&' + sa
        nothing_checked = False
    if nothing_checked:
        return render(request, "myadmin/info.html", {"info" : "You didn't select any days to edit for the course!"})
    days = days[1:]
    start_time = request.POST["start_time"]
    TIME = ""
    if start_time == 'a':
        TIME = "09:30 - 10:45"
    if start_time == 'b':
        TIME = "11:00 -12:15"
    if start_time == 'c':
        TIME = "11:00 -12:15"
    if start_time == 'd':
        TIME = "11:00 -12:15"
    sch.start_time = TIME
    sch.max_limit = request.POST["max_limit"]
    sch.days = days
    sch.iid = request.POST["iid"]
    sch.className = request.POST["classname"]
    sch.semester = request.POST["semester"]
    sch.save()
    context = {"info" : "Successfully Edited Course!"}
    
    return render(request, "myadmin/info.html", context)
