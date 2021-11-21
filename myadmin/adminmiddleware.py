#middleware protection
from django.shortcuts import redirect
from django.urls import reverse
import re

class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        #allowed url list
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin']
        if re.match(r'^/myadmin', path) and (path not in urllist):
            #check if alredy logged in(session will have the record)
            if 'adminuser' not in request.session:
                return redirect(reverse('myadmin_login'))

        response = self.get_response(request)
        return response