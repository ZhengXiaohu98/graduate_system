from django.shortcuts import render, redirect
from django.urls import reverse
from myadmin.models import student, schedules, instructor, course, period, stuCourse, waitList, stuMsg
from django.http import HttpResponse
import pickle


def search(request, check):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    schedulesObj = schedules.objects.all()
    
    terms = schedules.objects.values_list('year', 'semester').distinct()
    terms.query = pickle.loads(pickle.dumps(terms.query))
    courses = course.objects.all()
    days = schedules.objects.values_list('days').distinct()
    days.query = pickle.loads(pickle.dumps(days.query)) 
    times = schedules.objects.values_list('start_time').distinct()
    times.query = pickle.loads(pickle.dumps(times.query))
    
    # combine year and semester => term
    dataterms = []
    for i in terms:
        term = str(i["year"]) + " " + i["semester"]
        dataterms.append(term)

    
    if check == 1:
        context = {"userinfo":uinfo, "course": courses, "term":dataterms,"time":times, "day":days, "check":1}
    else:
        context = {"userinfo":uinfo, "course": courses, "term":dataterms,"time":times, "day":days, "check":0}

    return render(request, 'student/SearchCourse/search.html',context)


def searchmodify(request, search):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    schedulesObj = schedules.objects.all()
  
    terms = schedules.objects.values_list('year', 'semester').distinct()
    terms.query = pickle.loads(pickle.dumps(terms.query))
    courses = course.objects.all()
    days = schedules.objects.values_list('days').distinct()
    days.query = pickle.loads(pickle.dumps(days.query))
    times = schedules.objects.values_list('start_time').distinct()
    times.query = pickle.loads(pickle.dumps(times.query))
    
    if search == 1:
        info = "You must select something to proceed"
        context = {"userinfo": uinfo, "info":info, "search":search}
        return render(request, 'student/SearchCourse/searchmodify.html',context)


    search = search.split(",")

    # combine year and semester => term
    dataterms = []
    for i in terms:
        term = str(i["year"]) + " " + i["semester"]
        dataterms.append(term)

    context = {"userinfo":uinfo, "course": courses, "term":dataterms,"time":times, "day":days, 
            "mterm":search[0],"mcourse":search[1],"mday":search[2],"mtime":search[3], "mstatus":search[4]}
    
    return render(request, 'student/SearchCourse/searchmodify.html',context)


def courses(request, res):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # get the result from search    
    if (res == '0'):
        term = request.POST['term']
        classname = request.POST['course']
        day = request.POST['day']
        time = request.POST['time']
        status = request.POST['status']
        search = term + "," + classname + "," + day + "," + time + ","+ status

    # view search result that is already exist 
    else:
        x = res.split(",")
        term = x[0]
        classname = x[1]
        day = x[2]
        time = x[3]
        status = x[4]
        search = res

    # search for the course
    if term == 'Choose Term' and classname == 'Choose Course' and day == "Choose Day" and time == "Choose Time" and status == "Choose Status":
        return redirect(reverse('student_SearchCourse', args = (1,)))

    schedulesObj = schedules.objects.all()

    if term != 'Choose Term' :
        x = term.split()
        year = x[0]
        semester = x[1]
        schedulesObj = schedulesObj.filter(year = year, semester = semester)

    if classname != 'Choose Course':
        schedulesObj =schedulesObj.filter(className = classname)
    if day != 'Choose Day':
        schedulesObj =schedulesObj.filter(days = day)
    if time != 'Choose Time':
        schedulesObj =schedulesObj.filter(start_time = time)
    if status != 'Choose Status':
        schedulesObj =schedulesObj.filter(status = status)

      

    count = schedulesObj.count()
    # in case there is no course result found
    if count ==0:
        info = "No result found! Try to modify your search!"
        context = {"userinfo": uinfo, "info":info, "search":search}
        return render(request, 'student/SearchCourse/info.html',context)

    data=[]
    for obj in schedulesObj:
        insObj = instructor.objects.get(iid = obj.iid)
        courseObj = course.objects.get(className = obj.className)

        Cterm = str(obj.year) +' '+ str(obj.semester)
        Cperiod = period.objects.get(term = Cterm)
        
        #check if the course is already add to schedule or already add in waitlist
        pastCourse = stuCourse.objects.filter(sid = id, sectionNum = obj.sectionNum).count()
        waitlist = waitList.objects.filter(sid = id, sectionNum = obj.sectionNum).count()
        if pastCourse == 0 and waitlist == 0 :
             rlist = {"year":obj.year, "semester":obj.semester,"cid":courseObj.cid, "className":obj.className, 
            "section":obj.sectionNum,"insName":insObj.insName, "day":obj.days, "time":obj.start_time,
            "status":obj.status, "period":Cperiod.curPeriod, "Added": 0}
        else:
            rlist = {"year":obj.year, "semester":obj.semester,"cid":courseObj.cid, "className":obj.className, 
                "section":obj.sectionNum,"insName":insObj.insName, "day":obj.days, "time":obj.start_time,
                "status":obj.status, "period":Cperiod.curPeriod, "Added":1}

        data.append(rlist)
    
    context = {"userinfo":uinfo,"course": data, "search":search}
    return render(request, 'student/SearchCourse/courseslist.html',context)


def addview(request, section, search):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # get the couse infomation of the current adding class
    AddingCourse = schedules.objects.get(sectionNum = section)
    insObj = instructor.objects.get(iid = AddingCourse.iid)
    # get the prerequirement of current adding class
    courseObj = course.objects.get(className = AddingCourse.className)
    if courseObj.pre_req != 0 :
        prereq = course.objects.get(cid = courseObj.pre_req)
    else:
        prereq = 0

    # get the course in wait list
    waitlist = waitList.objects.filter(sid = id, year = AddingCourse.year, semester = AddingCourse.semester)
    if waitlist.count() == 0: # when there is not course in wait list
        wait = 0
    else:
        wait = []
        for obj in waitlist:
            schedulesObj = schedules.objects.get(sectionNum = obj.sectionNum)
            insObj = instructor.objects.get(iid = schedulesObj.iid)
            courseObj = course.objects.get(className = schedulesObj.className)

            rlist = {"cid": courseObj.cid, "className":schedulesObj.className, "section":schedulesObj.sectionNum,"insName":insObj.insName, 
            "day":schedulesObj.days, "time":schedulesObj.start_time,"position":obj.position}
            wait.append(rlist)


    # get the course already add for next term
    AddedCourse = stuCourse.objects.filter(sid = id, year = AddingCourse.year, semester = AddingCourse.semester)
    Added = AddedCourse.count()
    
    if Added == 0:
        info = "No Course Added"
        data = 0
    else:
        info = 0
        data = []
        for obj in AddedCourse:
            schedulesObj = schedules.objects.get(sectionNum = obj.sectionNum)
            insObj = instructor.objects.get(iid = schedulesObj.iid)
            courseObj = course.objects.get(className = schedulesObj.className)

            rlist = {"cid": courseObj.cid, "className":schedulesObj.className, "section":schedulesObj.sectionNum,"insName":insObj.insName, 
            "day":schedulesObj.days, "time":schedulesObj.start_time}

            data.append(rlist)
    
    context = {"userinfo": uinfo, "info":info, "addcourse":AddingCourse, "course":data , "year":AddingCourse.year,
             "semester":AddingCourse.semester, "instructor":insObj.insName, "prerequire": prereq, "search":search, "waitlist":wait}
    return render(request, 'student/SearchCourse/add.html',context)


def add(request, section, search):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # get all the course taking by student
    pastCourse = stuCourse.objects.filter(sid = id)

    # get the couse infomation of the current adding class
    AddingCourse = schedules.objects.get(sectionNum = section)

    #get the course id and pre-requirement 
    CourseObj = course.objects.get(className = AddingCourse.className)

    # get the course already add for next semester
    CourseNext = stuCourse.objects.filter(sid = id, year = AddingCourse.year, semester = AddingCourse.semester)

    # check if student current status is graduate or suspended
    if(uinfo.curStatus == 0):
        info = "You are currently suspended, you must pay the fine in order to register course for next semester."
        context = {"userinfo": uinfo, "info":info, "status":0, "search":search}
        return render(request, 'student/SearchCourse/addinfo.html',context)
    
    if(uinfo.curStatus == 2):
        info = "You are graduated student! You can't take any more courses."
        context = {"userinfo": uinfo, "info":info, "status":0, "search":search}
        return render(request, 'student/SearchCourse/addinfo.html',context)

    # check if the added course reach the limit
    addedNum = CourseNext.count()
    if(addedNum >= 4):
        info = "You cannot add more courses. You can only take 4 course per semester."
        context = {"userinfo": uinfo, "info":info, "status":0, "course":AddingCourse, "search":search}
        return render(request, 'student/SearchCourse/addinfo.html',context)


    # check meet prequirement
    if(CourseObj.pre_req != 0):
        preCourse = stuCourse.objects.filter(sid = id, cid = CourseObj.pre_req)
        preCourse2 = stuCourse.objects.filter(sid = id, cid = CourseObj.pre_req, year = AddingCourse.year, semester = AddingCourse.semester)
        
        if(preCourse.count() - preCourse2.count() == 0):
            #find the className of prequirement
            pre = course.objects.get(cid = CourseObj.pre_req)
            info = "Pre requirement is not meet, must take ("+ pre.className + ") before taking (" + CourseObj.className +")."
            context = {"userinfo": uinfo, "info":info, "status":0, "course":AddingCourse, "search":search}
            return render(request, 'student/SearchCourse/addinfo.html',context)

    # check if class is already taken
    for i in pastCourse:
        if (i.cid == str(CourseObj.cid) and i.grade != 'F'):
            if (i.year == AddingCourse.year and i.semester == AddingCourse.semester):
                info = "You already add (" + CourseObj.className + ") for next semester."
            else:
                info = "You already taken (" + CourseObj.className + ") in " + str(i.year) +" " + i.semester + "."
            context = {"userinfo": uinfo, "info":info, "status":0, "course":AddingCourse,"search":search}
            return render(request, 'student/SearchCourse/addinfo.html',context)
    
    # check time conflict
    for i in CourseNext:
        #get the schedule of course
        ScheduleObj = schedules.objects.get(sectionNum = i.sectionNum)

        if(AddingCourse.start_time == ScheduleObj.start_time and AddingCourse.days ==ScheduleObj.days):
            info = "Having time conflict with course (" + ScheduleObj.className +") You cannot take two course at a same time."
            context = {"userinfo": uinfo, "info":info, "status":0, "course":AddingCourse, "search":search}
            return render(request, 'student/SearchCourse/addinfo.html',context)

    # check if class is alreay full
    if (AddingCourse.current_enroll == AddingCourse.max_limit):
            #add person towaitlist
            AddingCourse.wait_list += 1
            AddingCourse.save()
            wait = waitList()
            wait.sid =id
            wait.year = AddingCourse.year
            wait.semester = AddingCourse.semester
            wait.sectionNum = AddingCourse.sectionNum
            wait.position = AddingCourse.wait_list
            wait.save()
            
            notification = stuMsg()
            notification.receiverID = id
            notification.sender = "System"
            notification.title = "Waitlist Position"
            notification.content = "Course ("+ AddingCourse.className +") is full. You current in wait list position: " + str(AddingCourse.wait_list)
            notification.save()

            info = "Course ("+ AddingCourse.className +") is full. You have been place to the wait list with current position : " + str(AddingCourse.wait_list)
            context = {"userinfo": uinfo, "info":info, "status":2, "course":AddingCourse, "search":search}
            return render(request, 'student/SearchCourse/addinfo.html',context)



    # No conflict
    add = stuCourse()
    add.sid = id
    add.cid = CourseObj.cid
    add.sectionNum = AddingCourse.sectionNum
    add.year = AddingCourse.year
    add.semester = AddingCourse.semester
    add.curStatus = 2   
    add.save()

    # add one person to current_enroll 
    AddingCourse.current_enroll += 1
    AddingCourse.save()

    info = "Course ("+ AddingCourse.className +") added to your schedule!"
    context = {"userinfo": uinfo, "info":info, "status":1, "course":AddingCourse, "search":search}
    return render(request, 'student/SearchCourse/addinfo.html',context)
        




