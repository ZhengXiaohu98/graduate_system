from django.urls import path
from myadmin.views import index, student, instructor, application, course

urlpatterns = [
    #myadmin index page
    path('', index.index, name = 'myadmin_index'),

    #login pages url
    path('login', index.login, name = 'myadmin_login'),
    path('dologin', index.dologin, name = 'myadmin_dologin'),
    path('logout', index.logout, name = 'myadmin_logout'),

    #student url page
    path('student/stuview/<int:pIndex>', student.viewStudent, name = 'student_view'),
    path('student/stuedit/<int:stuid>', student.editStudent, name = 'student_edit'),
    path('student/stuupdate', student.updateStudent, name = 'student_update'),
    path('student/stuadd', student.addStudent, name = 'student_add'),
    path('student/stuinsert', student.insertStudent, name = 'student_insert'),

    #instructor url page
    path('instructor/insview/<int:pIndex>', instructor.viewInstructor, name = 'instructor_view'),
    path('instructor/insedit/<int:insid>', instructor.editInstructor, name = 'instructor_edit'),
    path('instructor/insupdate', instructor.updateInstructor, name = 'instructor_update'),
    path('instructor/insadd', instructor.addInstructor, name = 'instructor_add'),
    path('instructor/insinsert', instructor.insertInstructor, name = 'instructor_insert'),

    #student applications url page
    path('application/student/<int:pIndex>', application.viewStuApp, name = 'stuapp_view'),
    path('application/student/appdeal/<int:stateid>', application.dealStuApp, name = 'stuapp_deal'),
    path('application/student/action/', application.actionStuApp, name = 'stuapp_action'),

    #instrctor applications url page
    path('application/instructor/<int:pIndex>', application.viewInsApp, name = 'insapp_view'),
    path('application/instructor/appdeal/<int:stateid>', application.dealInsApp, name = 'insapp_deal'),
    path('application/instructor/action/', application.actionInsApp, name = 'insapp_action'),

    #class url page
    path('course/courseview/<int:pIndex>', course.viewCourse, name = 'course_view'),
    path('course/courseadd', course.addCourse, name = 'course_add'),
    path('course/courseinsert', course.insertCourse, name = 'course_insert'),
    path('course/courseedit/<int:cid>', course.editCourse, name = 'course_edit'),
    path('course/courseupdate', course.updateCourse, name='course_update')
]