from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import adminManagement

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