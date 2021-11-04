from django.urls import path
from student.views import index, setting, complain, AcademicRecord, SearchCourses, courseManage

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

    path('CourseManage', courseManage.index, name = 'student_CourseManage'),

    #student current information url
    path('SearchCourse/<int:check>', SearchCourses.search, name = 'student_SearchCourse'),
    path('SearchCourse/modify/?P<search>', SearchCourses.searchmodify, name='SearchCourse_modify'),
    path('SearchCourse/courses', SearchCourses.courses, name='SearchCourse_courses'),

    #student Academic Record url
    path('AcademicRecord', AcademicRecord.index, name = 'student_AcademicRecord'),
    path('AcademicRecord/history', AcademicRecord.stuHistory, name = 'AcademicRecord_history'),
    path('AcademicRecord/graduate', AcademicRecord.stugraduate, name = 'AcademicRecord_graduate'),
    path('AcademicRecord/graduate/apply', AcademicRecord.applyGraudate, name = 'AcademicRecord_graduate_apply'),
    path('AcademicRecord/graduate/submit', AcademicRecord.submitGradate, name = 'AcademicRecord_graduate_submit'),

    #student complain url
    path('complain', complain.stuComplain, name = 'student_complain'),
    path('complain/stu/?P<info>?P<name>?P<description><int:pIndex>', complain.stuComplainStu, name = 'complain_student'),
    path('complain/stu/submit', complain.formSubmitStu, name = 'complain_student_submit'),
    path('complain/ins/?P<info>?P<name>?P<description><int:pIndex>', complain.stuComplainIns, name = 'complain_instructor'),
    path('complain/ins/submit', complain.formSubmitIns, name = 'complain_instructor_submit'),

    #student setting url
    path('setting', setting.show, name = 'student_setting'),
    path('setting/information', setting.information, name = 'student_setting_information'),
    path('setting/information/update', setting.infoupdate, name = 'student_setting_information_update'),
    path('setting/password', setting.password, name = 'student_setting_password'),
    path('setting/password/update', setting.updatepwd, name = 'student_setting_password_update'),

    
]