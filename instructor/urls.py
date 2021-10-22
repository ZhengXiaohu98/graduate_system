from django.urls import path
from instructor.views import index

urlpatterns = [
    #instructor index page
    path('', index.index, name = 'instructor_index'),

    #login pages url
    path('login', index.login, name = 'instructor_login'),
    path('dologin', index.dologin, name = 'instructor_dologin'),
    path('logout', index.logout, name = 'instructor_logout'),

    #instructor application url
    path('application', index.insApplications, name='instructor_application'),
    path('application/save', index.saveApplication, name='instructor_application_save'),
    path('application/check', index.checkApplication, name='instructor_application_check'),
    path('application/docheck', index.docheckApplication, name='instructor_application_docheck'),
]