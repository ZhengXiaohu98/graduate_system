from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student, stuApplication

#admin index page
def index(request):
    return render(request, 'student/index.html')

#admin login form
def login(request):
    return render(request, 'student/login.html')

def dologin(request):
    try:
        uname = request.POST.get('username')
        pw = request.POST.get('password')
        obj = student.objects.get(username = uname)
        correctPW = obj.pw
        if(pw != correctPW):
            context = {"msg" : "Incorrect password!"}
        else:
            request.session['studentuser'] = obj.toDict()
            return redirect(reverse('student_index'))
    except Exception as err:
        context = {"msg" : "Student Not Found!"}
    return render(request, 'student/login.html', context)

def logout(request):
    del request.session['studentuser']
    return redirect(reverse('student_login'))

def stuApplications(request):
    return render(request, 'student/stu_application.html')

def saveApplication(request):
    id = request.POST.get('id', None)
    stuName = request.POST.get('name', None)
    gender = request.POST.get('gender', None)
    stuGPA = request.POST.get('GPA', None)
    email = request.POST.get('email', None)
    extraInfo = request.POST.get('extraInfo', None)
    print(id, stuName, gender, stuGPA, email)
    if id is None or stuName is None or gender is None or stuGPA is None or email is None:
        return render(request, 'student/info.html', {"info":"You must fill the requiered field!"})
    obj = stuApplication()
    obj.stateid = id
    obj.stuName = stuName
    obj.gender = gender
    obj.GPA = (float)(stuGPA)
    obj.email = email
    obj.info = extraInfo
    obj.save()
    return render(request, 'student/info.html', {"info":"Applied successfully! You can use your state ID to check your application!"})

def checkApplication(request):
    return render(request, 'student/stu_application_check.html', {'info':''})

def docheckApplication(request):
    id = request.POST['id']
    try:
        obj = stuApplication.objects.get(stateid = id)
    except:
        return render(request, 'student/stu_application_check.html', {'info':'No application found!'})
    return render(request, 'student/stu_application_status.html', {'stuApp':obj})