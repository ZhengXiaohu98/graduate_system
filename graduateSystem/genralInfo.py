from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls.resolvers import RegexPattern
from myadmin.models import student, schedules

def generalInfo(request):
    students = student.objects.all().order_by("-GPA")[:5]
    data=[]
    for s in students:
        slist = {"stuName":s.stuName, "GPA":s.GPA, "sid":s.sid}
        data.append(slist)

    goodRatingObj = schedules.objects.all().order_by("-rating")[:5]
    badRatingObj = schedules.objects.all().order_by("rating")[:5]
    
    good =[]
    for g in goodRatingObj:
        glist = {"sectionNum":g.sectionNum, "className":g.className, "year":g.year,"semester":g.semester,
                  "iid":g.iid,"rating":g.rating}
        good.append(glist)

    bad =[]
    for b in badRatingObj:
        blist = {"sectionNum":b.sectionNum, "className":b.className, "year":b.year,"semester":b.semester,
                  "iid":b.iid,"rating":b.rating}
        bad.append(blist)

    context = {"topStudent":data,"goodRating":good, "badRating":bad}
    return render(request, "generalInfo.html",context)