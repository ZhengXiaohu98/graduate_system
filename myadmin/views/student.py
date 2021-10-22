from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import student

#view student table page
def viewStudent(request, pIndex=1):
    stuList = student.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        stuList = stuList.filter(Q(stuName__contains=kw) | Q(username__contains=kw) | Q(gender__contains=kw) | Q(email__contains=kw) | Q(GPA__contains=kw))
        myKey.append('keyword='+kw)
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(stuList, 10)
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

    context = {"stulist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey}
    return render(request, "myadmin/student/viewstudent.html", context)

#edit student page
def editStudent(request, stuid = 0):
    try:
        obj = student.objects.get(sid = stuid)
        print(stuid)
        context = {"stu" : obj}
        return render(request, "myadmin/student/editstudent.html", context)
    except:
        context = {"info" : "Error edit student!"}
        return render(request, "myadmin/info.html", context)

#update the form submitted by edit student page
def updateStudent(request):
    try:
        obj = student.objects.get(sid = request.POST['sid'])
        obj.username = request.POST['username']
        obj.pw = request.POST['password']
        obj.name = request.POST['name']
        obj.gender = request.POST['gender']
        obj.email = request.POST['email']
        stat = request.POST['status']
        if stat == 'S':
            obj.curStatus = 0
        elif stat == 'N':
            obj.curStatus = 1
        else:
            obj.curStatus = 2
        obj.save()
        context = {"info" : "Edit student success!"}
    except:
        context = {"info" : "Edit student fail!"}
    return render(request, "myadmin/info.html", context)

#add student page
def addStudent(request):
    name = request.POST.get("name", "")
    gender = request.POST.get("gender", "")
    email = request.POST.get("email", "")
    context = {"name":name, "gender":gender, "email":email}
    return render(request, "myadmin/student/addstudent.html", context)

#insert the student info
def insertStudent(request):
    try:
        #get the student information from the page
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]
        gender = request.POST["gender"]
        email = request.POST["email"]

        #check if username is already used
        obj = student.objects.filter(username = username)
        if obj.count() == 1:
            return render(request, "myadmin/info.html", {"info" : "Add student fail, username already exist!"})
        #save the student in the database
        newStu = student()
        newStu.stuName = name
        newStu.username = username
        newStu.pw = password
        newStu.gender = gender
        newStu.email = email
        newStu.curStatus = 1
        newStu.save()
        context = {"info" : "Successfully added student!"}
    except:
        context = {"info" : "Failed to add student!"}
    return render(request, "myadmin/info.html", context)