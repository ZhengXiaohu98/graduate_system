from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls.resolvers import RegexPattern
from myadmin.models import student, schedules, instructor

def generalInfo(request):
    students = student.objects.all().order_by("-GPA")[:5]
    data=[]
    for s in students:
        slist = {"stuName":s.stuName, "GPA":s.GPA, "sid":s.sid}
        data.append(slist)

    goodRatingObj = schedules.objects.all().order_by("-rating")[:5]
    badRatingObj = schedules.objects.filter(rating__gte=0).order_by("rating")[:5]
    
    good =[]
    for g in goodRatingObj:
        insName = instructor.objects.get(iid = g.iid).insName
        glist = {"sectionNum":g.sectionNum, "className":g.className, "year":g.year,"semester":g.semester,
                  "insName":insName,"rating":g.rating}
        good.append(glist)

    bad =[]
    for b in badRatingObj:
        insName = instructor.objects.get(iid = b.iid).insName
        blist = {"sectionNum":b.sectionNum, "className":b.className, "year":b.year,"semester":b.semester,
                  "insName":insName,"rating":b.rating}
        bad.append(blist)
        print(blist["rating"])
        print(blist["insName"])
    

    context = {"topStudent":data,"goodRating":good, "badRating":bad}
    return render(request, "generalInfo.html",context)