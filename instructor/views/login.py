from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import instructor, insApplication

#instructor login form
def login(request):
    return render(request, 'instructor/login.html')

def dologin(request):
    try:
        uname = request.POST.get('username')
        pw = request.POST.get('password')
        obj = instructor.objects.get(username = uname)
        correctPW = obj.pw
        if(pw != correctPW):
            context = {"msg" : "Incorrect password!"}
        else:
            request.session['instructoruser'] = obj.toDict()
            return redirect(reverse('instructor_index'))
    except Exception as err:
        context = {"msg" : "Instructor Not Found!"}
    return render(request, 'instructor/login.html', context)

def logout(request):
    del request.session['instructoruser']
    return redirect(reverse('instructor_login'))
