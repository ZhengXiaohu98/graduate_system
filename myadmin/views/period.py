from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import period

#view complain table page
def viewPeriod(request):
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    context = {"cur":cur, "uc":uc}
    return render(request, "myadmin/period/viewperiod.html", context)

def nextPeriod(request):
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    if cur.curPeriod == 5:
        return render(request, "myadmin/info.html", {"info" : "It is the last period of the term. You can only end the term!"})
    cur.curPeriod += 1
    if cur.curPeriod == 4:
        uc.curPeriod = 1
    if cur.curPeriod == 5:
        uc.curPeriod = 2
    cur.save()
    uc.save()
    return render(request, "myadmin/info.html", {"info" : "Successfully updated the period!"})

def endPeriod(request):
    cur = period.objects.get(curStatus=2)
    uc = period.objects.get(curStatus=1)
    if cur.curPeriod != 5:
        return render(request, "myadmin/info.html", {"info" : "You cannot end the term before having a grading period!"})
    cur.curStatus = -1
    uc.curStatus = 2
    nextTerm = period.objects.get(pid = uc.pid + 1)
    nextTerm.curStatus = 1
    cur.save()
    uc.save()
    nextTerm.save()
    return render(request, "myadmin/info.html", {"info" : "Successfully ended term!"})