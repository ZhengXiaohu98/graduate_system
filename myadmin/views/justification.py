from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import justification

#view graduate table page
def viewJust(request, pIndex=1):
    justList = justification.objects.all()
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(justList, 10)
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
    context = {"justlist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex}
    return render(request, "myadmin/justification/viewjustification.html", context)

def dealJust(request, jjid):
    curJust = justification.objects.get(jid = jjid)
    curJust.curStatus = 1
    curJust.save()
    return render(request, "myadmin/justification/curjustification.html", {"cur" : curJust})
