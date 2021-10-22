from django.urls import path
from student.views import index

urlpatterns = [
    #student index page
    path('', index.index, name = 'student_index'),

    #login pages url
    path('login', index.login, name = 'student_login'),
    path('dologin', index.dologin, name = 'student_dologin'),
    path('logout', index.logout, name = 'student_logout'),

    #student application url
    path('application', index.stuApplications, name = 'student_application'),
    path('application/save', index.saveApplication, name='student_application_save'),
    path('application/check', index.checkApplication, name='student_application_check'),
    path('application/docheck', index.docheckApplication, name='student_application_docheck'),
]