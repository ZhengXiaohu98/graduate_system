from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import complainmsg, student, instructor

#view student table page
def viewComplain(request, pIndex = 1):
    cpList = complainmsg.objects.all()
    #keep the serach keyword
    myKey = []
    #get the serach keyword
    kw = request.GET.get('keyword', None)
    if kw is not None:
        cpList = cpList.filter(Q(id__contains=kw) | Q(fromId__contains=kw) | Q(fromName__contains=kw) | Q(receiveId__contains=kw) | Q(receiveName__contains=kw))
        myKey.append('keyword='+kw)
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(cpList, 10)
    maxPages = p.num_pages
    #check if exceed the page limit or invalid page index
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    # get the cur list
    retList = p.page(pIndex)
    #get the page range
    pRange = p.page_range

    context = {"cplist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex, "myKey":myKey}
    return render(request, "myadmin/complain/viewcomplain.html", context)

def dealComplain(request, cpid):
    cur = complainmsg.objects.get(id = cpid)
    return render(request, "myadmin/complain/dealcomplain.html", {"cur" : cur})

def updateComplain(request):
    cpid = request.POST["cpid"]
    cur = complainmsg.objects.get(id = cpid)
    
    if cur.curStatus != 0:
        return render(request, "myadmin/info.html", {"info" : "The Complain Message was viewed already!"})
    
    if 'approve' in request.POST:
        cur.curStatus = 1
        if cur.receiveType == 'Student':
            curStu = student.objects.get(sid = cur.receiveId)
            curStu.cp_num += 1
            cur.save()
            curStu.save()
        if cur.receiveType == 'Instructor':
            curIns = instructor.objects.get(iid = cur.receiveId)
            curIns.cp_num += 1
            cur.save()
            curIns.save()
        return render(request, "myadmin/info.html", {"info" : "Complain  message approved successfully!"})
    
    if 'reject' in request.POST:
        cur.curStatus = 2
        cur.save()
        return render(request, "myadmin/info.html", {"info" : "Complain  message rejected successfully!"})