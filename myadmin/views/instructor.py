from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import instructor

#view student table page
def viewInstructor(request, pIndex=1):
    insList = instructor.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        insList = insList.filter(Q(insName__contains=kw) | Q(username__contains=kw) | Q(gender__contains=kw) | Q(email__contains=kw))
        myKey.append('keyword='+kw)
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(insList, 10)
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

    context = {"inslist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey}
    return render(request, "myadmin/instructor/viewinstructor.html", context)

#edit instructor page
def editInstructor(request, insid = 0):
    try:
        obj = instructor.objects.get(iid = insid)
        context = {"ins" : obj}
        return render(request, "myadmin/instructor/editinstructor.html", context)
    except:
        context = {"info" : "Error edit instructor!"}
        return render(request, "myadmin/info.html", context)

#update the form submitted by edit instructor page
def updateInstructor(request):
    try:
        obj = instructor.objects.get(iid = request.POST['iid'])
        obj.username = request.POST['username']
        obj.pw = request.POST['password']
        obj.name = request.POST['name']
        obj.gender = request.POST['gender']
        obj.email = request.POST['email']
        stat = request.POST['status']

        if stat == 'S':
            obj.curStatus = 0
        else:
            obj.curStatus = 1
        obj.save()

        context = {"info" : "Edit instructor success!"}
    except:
        context = {"info" : "Edit instructor fail!"}
    return render(request, "myadmin/info.html", context)

#add Instructor page
def addInstructor(request):
    name = request.POST.get("name", "")
    gender = request.POST.get("gender", "")
    email = request.POST.get("email", "")
    context = {"name":name, "gender":gender, "email":email}
    return render(request, "myadmin/instructor/addInstructor.html", context)

#insert the instructor info
def insertInstructor(request):
    try:
        #get the instructor information from the page
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]
        gender = request.POST["gender"]
        email = request.POST["email"]

        #check if username is already used
        obj = instructor.objects.filter(username = username)
        if obj.count() == 1:
            return render(request, "myadmin/info.html", {"info" : "Add instructor fail, username already exist!"})
        #save the instructor in the database
        newIns = instructor()
        newIns.insName = name
        newIns.username = username
        newIns.pw = password
        newIns.gender = gender
        newIns.email = email
        newIns.curStatus = 1
        newIns.save()
        context = {"info" : "Successfully added instructor!"}
    except:
        context = {"info" : "Failed to add instructor!"}
    return render(request, "myadmin/info.html", context)