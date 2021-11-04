#middleware protection
from django.shortcuts import redirect
from django.urls import reverse
import re

class StudentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        #allowed url list
        urllist = ['/student/login', '/student/logout', '/student/dologin', '/student/application', '/student/application/save', '/student/info', 
        '/student/application/check', '/student/application/docheck']
        if re.match(r'^/student', path) and (path not in urllist):
            #check if alredy logged in(session will have the record)
            if 'studentuser' not in request.session:
                return redirect(reverse('student_login'))



        response = self.get_response(request)
        return response