from django.urls import path
from instructor.views import courseList, index, application, login, profile, complain, notification

urlpatterns = [
    #instructor index page
    path('', index.index, name = 'instructor_index'),
    path('justificatonInfo', index.sendJustification, name = 'justification'),


    #login pages url
    path('login', login.login, name = 'instructor_login'),
    path('dologin', login.dologin, name = 'instructor_dologin'),
    path('logout', login.logout, name = 'instructor_logout'),

    #instructor application url
    path('application', application.insApplications, name='instructor_application'),
    path('application/save', application.saveApplication, name='instructor_application_save'),
    path('application/check', application.checkApplication, name='instructor_application_check'),
    path('application/docheck', application.docheckApplication, name='instructor_application_docheck'),

    #instructor profile update url
    path('profile/edit', profile.editProfile, name='profile_edit'),
    path('profile/update', profile.updateProfile, name='profile_update'),

    #instructor course list url
    path('courselist', courseList.viewCourse, name='course_list'),
    path('courselist/students/<int:sectionNum>', courseList.stuInCourse, name='stuInCourse'),
    path('courselist/students/<int:sectionNum>/gradeupdate', courseList.gradeUpdate, name='grade_update'),
    path('waitlist/students/<int:sectionNum>', courseList.viewWaitlist, name='viewWaitlist'),
    path('waitlist/students/waitlistUpdate/<int:sid>', courseList.waitlistUpdate, name='waitlistUpdate'),
    
    #complain page url
    path('complain/<int:pIndex>', complain.editComplain, name='complain'),
    path('complain/update', complain.updateComplain, name='update_complain'),

    #notification page
    path('notification/<int:pIndex>', notification.Notification, name='notification'),
    path('notification/update',notification.sendNotification, name='notificationUpdate')
]
    