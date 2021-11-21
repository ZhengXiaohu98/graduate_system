from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import adminManagement, instructor, student, insMsg, stuMsg

#admin index page
def index(request):
    return render(request, 'myadmin/index.html')

#admin login form
def login(request):
    return render(request, 'myadmin/login.html')

def dologin(request):
    try:
        uname = request.POST.get('username')
        pw = request.POST.get('password')
        obj = adminManagement.objects.get(username = uname)
        correctPW = obj.pw
        if(pw != correctPW):
            context = {"msg" : "Incorrect password!"}
        else:
            request.session['adminuser'] = obj.toDict()
            return redirect(reverse('myadmin_index'))
    except Exception as err:
        context = {"msg" : "User Not Found!"}
    return render(request, 'myadmin/login.html', context)

def logout(request):
    del request.session['adminuser']
    return redirect(reverse('myadmin_login'))

def sendNotifications(request):
    sendType = request.POST['type']
    title = request.POST['title']
    content = request.POST['content']
    print(sendType)
    if sendType == 'All' or sendType == 'Student':
        sendToStudent(title, content)
    if sendType == 'All' or sendType == 'Instructor':
        sendToInstructor(title, content)
    return render(request, 'myadmin/info.html', {"info" : "Notification is sent!"})
    
def sendToStudent(title, content):
    stuList = student.objects.all()
    for s in stuList:
        obj = stuMsg()
        obj.receiverID = s.sid
        obj.sender = "Administrator"
        obj.title = title
        obj.content = content
        obj.save()
    
    
def sendToInstructor(title, content):
    insList = instructor.objects.all()
    for i in insList:
        obj = insMsg()
        obj.receiverID = i.iid
        obj.title = title
        obj.content = content
        obj.save()
    