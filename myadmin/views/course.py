from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import course, instructor

def viewCourse(request, pIndex=1):
    courseList = course.objects.all()
    insList = instructor.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        courseList = courseList.filter(Q(cid__contains=kw) | Q(className__contains=kw) | Q(days__contains=kw))
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

    context = {"courselist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey, "insList":insList}
    return render(request, "myadmin/course/view_course.html", context)

def addCourse(request):
    insList = instructor.objects.all()
    return render(request, "myadmin/course/add_course.html", {"insList":insList})

def insertCourse(request):
    cid = request.POST["cid"]
    classname = request.POST["classname"]
    iid = request.POST["iid"]
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
    duration = request.POST["duration"]
    max_limit = request.POST["max_limit"]

    #save the course in the database
    newCourse = course()
    newCourse.cid = cid
    newCourse.className = classname
    newCourse.iid = (int)(iid)
    newCourse.days = days
    newCourse.start_time = ord(start_time) - 97
    newCourse.duration = duration
    newCourse.max_limit = max_limit
    newCourse.save()
    context = {"info" : "Successfully added Course!"}
    
    return render(request, "myadmin/info.html", context)

def editCourse(request, cid):
    try:
        insList = instructor.objects.all()
        obj = course.objects.get(cid = cid)
        context = {"course" : obj, "insList":insList}
        return render(request, "myadmin/course/edit_course.html", context)
    except:
        context = {"info" : "Error edit Course!"}
        return render(request, "myadmin/info.html", context)

def updateCourse(request):
    obj = course.objects.get(cid = request.POST['cid'])
    obj.className = request.POST["classname"]
    obj.iid = request.POST["iid"]
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
    obj.start_time = ord(request.POST["start_time"]) - ord('a')
    obj.duration = request.POST["duration"]
    obj.max_limit = request.POST["max_limit"]
    obj.days = days
    obj.save()
    context = {"info" : "Successfully Edited Course!"}
    
    return render(request, "myadmin/info.html", context)
