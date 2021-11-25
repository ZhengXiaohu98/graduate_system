from django.urls import path
from student.views import index, setting, complain, AcademicRecord, SearchCourses, courseManage

urlpatterns = [
    #student index page
    path('<int:pIndex>', index.index, name = 'student_index'),
    path('notification/<int:MsgId>', index.notification, name = 'student_notification'),
    path('review/<int:section>', index.reviewForm, name = 'student_review'),
    path('review/submit/<int:section>', index.reviewUpdate, name = 'student_review_submit'),
    path('payfine', index.pay, name = 'student_payfine'),
    path('payfine/submit',index.submitpay, name = 'student_payfine_submit'),

    #login pages url
    path('login', index.login, name = 'student_login'),
    path('dologin', index.dologin, name = 'student_dologin'),
    path('logout', index.logout, name = 'student_logout'),

    #student application url
    path('application', index.stuApplications, name = 'student_application'),
    path('application/save', index.saveApplication, name='student_application_save'),
    path('application/check', index.checkApplication, name='student_application_check'),
    path('application/docheck', index.docheckApplication, name='student_application_docheck'),

    #student course management url
    path('CourseManage', courseManage.index, name = 'student_CourseManage'),
    path('CourseManage/confirm/<int:section>', courseManage.confirmdrop, name = 'CourseManage_confirm'),
    path('CourseManage/confirm/drop/<int:section>', courseManage.drop, name = 'CourseManage_drop'),

    #student course search url
    path('SearchCourse/<int:check>', SearchCourses.search, name = 'student_SearchCourse'),
    path('SearchCourse/modify/?P<search>', SearchCourses.searchmodify, name='SearchCourse_modify'),
    path('SearchCourse/courses/?P<res>', SearchCourses.courses, name='SearchCourse_courses'),
    path('SearchCourse/courses/info/<int:section>?P<search>', SearchCourses.addview, name='SearchCourse_courses_info'),
    path('SearchCourse/courses/add/<int:section>?P<search>', SearchCourses.add, name='SearchCourse_courses_add'),

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