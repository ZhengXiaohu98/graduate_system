from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import payFine

#view graduate table page
def viewFines(request, pIndex=1):
    fineList = payFine.objects.all()
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(fineList, 10)
    maxPages = p.num_pages
    #check if exceed the page limit or invalid page index
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    # get the cur list
    fineList = p.page(pIndex)
    #get the page range
    pRange = p.page_range
    context = {"fineList":fineList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex}
    return render(request, "myadmin/studentfine/viewfine.html", context)

