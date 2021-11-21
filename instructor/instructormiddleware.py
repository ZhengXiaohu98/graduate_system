#middleware protection
from django.shortcuts import redirect
from django.urls import reverse
import re

class InstructorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        #allowed url list
        urllist = ['/instructor/login', '/instructor/logout', '/instructor/dologin', '/instructor/application', '/instructor/application/save', '/instructor/info', 
        '/instructor/application/check', '/instructor/application/docheck']
        if re.match(r'^/instructor', path) and (path not in urllist):
            #check if alredy logged in(session will have the record)
            if 'instructoruser' not in request.session:
                return redirect(reverse('instructor_login'))

        response = self.get_response(request)
        return response