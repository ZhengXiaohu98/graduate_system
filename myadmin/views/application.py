from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import stuApplication, insApplication

def viewStuApp(request, pIndex=1):
    stuAppList = stuApplication.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        stuAppList = stuAppList.filter(Q(stateid__contains=kw) | Q(stuName__contains=kw) | Q(gender__contains=kw) | Q(email__contains=kw) | Q(GPA__contains=kw))
        myKey.append('keyword='+kw)
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(stuAppList, 10)
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

    context = {"stuApplist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey}
    return render(request, "myadmin/application/view_stuapp.html", context)

def dealStuApp(request, stateid=0):
    obj = stuApplication.objects.get(stateid = stateid)
    return render(request, "myadmin/application/action_stuapp.html", {"appStu":obj})

def actionStuApp(request):
    id = request.POST["id"]
    obj = stuApplication.objects.get(stateid = id)
    if "rejt"  in request.POST:
        obj.curStatus = 2
        obj.save()
        return render(request, "myadmin/info.html", {"info":"student application rejected successfully!"})
    obj.curStatus = 1
    obj.save()
    name = request.POST["name"]
    gender = request.POST["gender"]
    email = request.POST["email"]
    context = {"name":name, "gender":gender, "email":email}
    return render(request, "myadmin/student/addstudent.html", context)

def viewInsApp(request, pIndex=1):
    insAppList = insApplication.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        insAppList = insAppList.filter(Q(stateid__contains=kw) | Q(insName__contains=kw) | Q(gender__contains=kw) | Q(email__contains=kw))
        myKey.append('keyword='+kw)
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(insAppList, 10)
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

    context = {"insAppList":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey}
    return render(request, "myadmin/application/view_insapp.html", context)

def dealInsApp(request, stateid=0):
    obj = insApplication.objects.get(stateid = stateid)
    return render(request, "myadmin/application/action_insapp.html", {"appIns":obj})

def actionInsApp(request):
    id = request.POST["id"]
    obj = insApplication.objects.get(stateid = id)
    if "rejt"  in request.POST:
        obj.curStatus = 2
        obj.save()
        return render(request, "myadmin/info.html", {"info":"instructor application rejected successfully!"})
    obj.curStatus = 1
    obj.save()
    name = request.POST["name"]
    gender = request.POST["gender"]
    email = request.POST["email"]
    context = {"name":name, "gender":gender, "email":email}
    return render(request, "myadmin/instructor/addinstructor.html", context)
