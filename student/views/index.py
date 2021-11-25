from django.shortcuts import render, redirect
from django.urls import reverse
<<<<<<< HEAD
from myadmin.models import student, stuApplication, stuCourse, schedules, instructor, period, review, stuMsg, payFine
from datetime import datetime
from django.core.paginator import Paginator 
import pickle

#admin index page
def index(request, pIndex):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # get the current term
    currentTerm = period.objects.get(curStatus = 2)
    print(currentTerm.curPeriod)


    # get the notification
    notification = stuMsg.objects.filter(receiverID = id).order_by('getTime').reverse()
    if (notification.count() == 0):
        notify = 0
    else:
        notify =[]
        for i in notification:
            if i.status == 0:
                show = "UNREAD"
            else:
                show = "READ"
            rlist = {"nid":i.nid, "time":i.getTime, "sender": i.sender, "title": i.title, "content":i.content, "status":show}
            notify.append(rlist)

        p = Paginator(notify, 5) 

        if(pIndex < 1):
            pIndex = 1
        if(pIndex > p.num_pages):
            pIndex = p.num_pages

        notify = p.page(pIndex)

    
    # get the current taking courses
    courseObj = stuCourse.objects.filter(sid = id ,curStatus = 2)

    # check if currents status of student is suspended
    if uinfo.curStatus == 0:
        info = "! ! Your current status is suspended ! !"
        context = {"userinfo":uinfo, "info":info , "taking":0, "Cperiod":currentTerm.curPeriod,"notification":notify}

    # check if student currently not taking course
    elif(courseObj.count() == 0 ):
        info = "! ! There is no current taking courses ! !"
        context = {"userinfo":uinfo, "info":info , "taking":0,"Cperiod":currentTerm.curPeriod, "notification":notify}

    
    else:
        # if there is exist course, return 0 for info
        info = 0
=======
from myadmin.models import student, stuApplication, stuCourse, schedules, instructor
import pickle

#admin index page
def index(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    if uinfo.curStatus == 0:
        info = "! ! Your current status is suspended ! !"
        context = {"userinfo":uinfo, "info":info , "taking":0}
        return render(request, 'student/index.html',context)

    try:
        # get the current taking courses
        courseObj = stuCourse.objects.filter(sid = id ,curStatus = 2)
        # get current term
        terms = courseObj.values_list('year', 'semester').distinct()
        terms.query = pickle.loads(pickle.dumps(terms.query))

        for i in terms:
            term= str(i["year"]) + " " + i["semester"]
>>>>>>> b5990fff3592c6072827bd6e368b8735286a81de

        # get the course inforation from schedule table
        data=[]
        for i in courseObj:
<<<<<<< HEAD
            if(i.grade == 'W'):
                continue
            schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
            ins = instructor.objects.get(iid = schedulesObj.iid)
            rlist ={"year":i.year, "semester":i.semester, "cid":i.cid ,"className":schedulesObj.className, "section":i.sectionNum, 
                        "insName":ins.insName, "day":schedulesObj.days, "time":schedulesObj.start_time}
            data.append(rlist)


        context = {"userinfo":uinfo, "info":info, "term": currentTerm.term, "course":data, "Cperiod":currentTerm.curPeriod, "taking":1, 
        "notification":notify}
    
    if(notify != 0):
        context["pIndex"] = pIndex
        context["pagelist"] = p.page_range

    return render(request, 'student/index.html',context)
    

# view notifcation in detail
def notification(request, MsgId):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    notification = stuMsg.objects.get(nid = MsgId)
    notification.status = 1
    notification.save()

    context = {"userinfo":uinfo, "notification":notification}

    return render(request, 'student/Main/notification.html',context)

# review page for a course
def reviewForm(request, section):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # get current reviewing course infomation
    Rcourse = schedules.objects.get(sectionNum = section)
    insObj = instructor.objects.get(iid = Rcourse.iid)

    # get the review history
    Rhistory = review.objects.filter(sid = id).order_by('createdTime').reverse()
    data = []
    if(Rhistory.count() == 0):
        data = 0
    else:
        for Rcourse in Rhistory:
            schedulesObj = schedules.objects.get(sectionNum = Rcourse.sectionNum)

            rlist = {"term": str(schedulesObj.year) + " "+ schedulesObj.semester, "className":schedulesObj.className,
            "section":Rcourse.sectionNum, "rating":Rcourse.rating, "Date":Rcourse.createdTime}
            data.append(rlist)

    context = {"userinfo":uinfo, "section":section, "course":Rcourse, "instructor":insObj.insName, "History":data}
    return render(request, 'student/Main/review.html',context)

# update review
def reviewUpdate(request, section):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    # check if student already submitted a review
    Rhistory = review.objects.filter(sid = id, sectionNum = section)

    if(Rhistory.count() == 1): # if review submitted , replace the rating and content
        Remove = review.objects.get(sid = id, sectionNum = section)
        Remove.delete()

    # add a new review
    Rcourse = review()
    Rcourse.sid = id
    Rcourse.sectionNum = section
    Rcourse.rating = request.POST['rating']
    Rcourse.content = request.POST['content']
    Rcourse.save()

    info = "Review for Section # " + str(section) + " Submitted!"
    context = {"userinfo":uinfo,"info":info, "section":section }
    return render(request, 'student/Main/info.html',context)

def pay(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)

    fine = payFine.objects.get(sid = id)

    context = {"userinfo":uinfo, "fine":fine, "remain":float(fine.amount-fine.paid), "info":0}
    return render(request, 'student/Main/payFine.html',context)

def submitpay(request):
    id = request.session['studentuser']['sid']
    uinfo = student.objects.get(sid = id)
    
    try:
        Upaid = request.POST['PayAmount']
        Ufine = payFine.objects.get(sid = id)
        Ufine.paid += float(Upaid)

        if (Ufine.paid == Ufine.amount):
            Ufine.status = 1
        Ufine.save()

        notification = stuMsg()
        notification.receiverID = id
        notification.sender = "System"
        notification.title = "Payment"
        notification.content = "Payment Complete!  Payment Amount: $ " + Upaid + ".  It will take 3 - 5 days to confirm your payment."
        notification.save()

        info = "Payment Complete! It will take 3 - 5 days to confirm your payment."
        context = {"userinfo":uinfo, "info":info}
        return render(request, 'student/Main/info.html',context)
    except Exception as err:
        fine = payFine.objects.get(sid = id)
        info = "Payment Amount Cannot Be Empty!"
        context = {"userinfo":uinfo, "fine":fine, "remain":float(fine.amount-fine.paid),"info":info}
    return render(request, 'student/Main/payfine.html', context)

=======
            schedulesObj = schedules.objects.get(sectionNum = i.sectionNum)
            ins = instructor.objects.get(iid = schedulesObj.iid)
            rlist ={"year":i.year, "semester":i.semester, "cid":i.cid ,"className":schedulesObj.className, "section":i.sectionNum, 
                    "insName":ins.insName, "day":schedulesObj.days, "time":schedulesObj.start_time}
            data.append(rlist)

        context = {"userinfo":uinfo, "term": term, "course":data, "taking":1}
        return render(request, 'student/index.html',context)
    except Exception as err:
        info = "! ! There is no current taking courses ! !"
        context = {"userinfo":uinfo, "info":info , "taking":0}
        return render(request, 'student/index.html',context)
>>>>>>> b5990fff3592c6072827bd6e368b8735286a81de

#admin login form
def login(request):
    return render(request, 'student/login.html')

def dologin(request):
    try:
        uname = request.POST.get('username')
        pw = request.POST.get('password')
        obj = student.objects.get(username = uname)
        correctPW = obj.pw
        if(pw != correctPW):
            context = {"msg" : "Incorrect password!"}
        else:
            request.session['studentuser'] = obj.toDict()
<<<<<<< HEAD
            return redirect(reverse('student_index', args = (1,)))
=======
            return redirect(reverse('student_index'))
>>>>>>> b5990fff3592c6072827bd6e368b8735286a81de
    except Exception as err:
        context = {"msg" : "Student Not Found!"}
    return render(request, 'student/login.html', context)
    

def logout(request):
    del request.session['studentuser']
    return redirect(reverse('student_login'))

def stuApplications(request):
    return render(request, 'student/stu_application.html')

def saveApplication(request):
    id = request.POST.get('id', None)
    stuName = request.POST.get('name', None)
    gender = request.POST.get('gender', None)
    stuGPA = request.POST.get('GPA', None)
    email = request.POST.get('email', None)
    extraInfo = request.POST.get('extraInfo', None)
    print(id, stuName, gender, stuGPA, email)
    if id is None or stuName is None or gender is None or stuGPA is None or email is None:
        return render(request, 'student/info.html', {"info":"You must fill the requiered field!"})
    obj = stuApplication()
    obj.stateid = id
    obj.stuName = stuName
    obj.gender = gender
    obj.GPA = (float)(stuGPA)
    obj.email = email
    obj.info = extraInfo
    obj.save()
    return render(request, 'student/info.html', {"info":"Applied successfully! You can use your state ID to check your application!"})

def checkApplication(request):
    return render(request, 'student/stu_application_check.html', {'info':''})

def docheckApplication(request):
    id = request.POST['id']
    try:
        obj = stuApplication.objects.get(stateid = id)
    except:
        return render(request, 'student/stu_application_check.html', {'info':'No application found!'})
    return render(request, 'student/stu_application_status.html', {'stuApp':obj})