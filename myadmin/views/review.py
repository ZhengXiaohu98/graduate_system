from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import review, student, stuMsg, payFine

#view graduate table page
def viewReview(request, pIndex=1):
    revtList = review.objects.all()
    #divide pages
    pIndex = int(pIndex)
    p = Paginator(revtList, 10)
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
    context = {"revlist":retList, "pRange":pRange, "maxPages":maxPages, "pIndex":pIndex}
    return render(request, "myadmin/review/viewreview.html", context)

def dealReview(request, rrid):
    tList = ["bitch", "Bitch", "dumb", "Dumb", "dogshit", "Dogshit", "shit", "Shit", "fuck", "Fuck", "ass", "Ass", "ugly", "Ugly", "Motherfuker", "motherfuker"]
    curReview = review.objects.get(rid = rrid)
    checkStr = curReview.content
    twCnt = 0
    for tw in tList:
        if checkStr.find(tw) != -1:
            checkStr = checkStr.replace(tw, "***")
            twCnt = twCnt + 1
            print(twCnt)
    curReview.content = checkStr
    
    curStu = student.objects.get(sid = curReview.sid)
    CONTENT = ""
    if twCnt < 3 and twCnt > 0:
        curStu.cp_num = curStu.cp_num + 1
        CONTENT = "You have received one warning because your review contains taboo words!"
    if twCnt >= 3:
        curStu.cp_num = curStu.cp_num + 2
        CONTENT = "You have received TWO warnings because your review contains more than 2 taboo words!"
    
    if twCnt != 0:
        curStuMsg = stuMsg()
        curStuMsg.receiverID = curStu.sid
        curStuMsg.sender = "Register"
        curStuMsg.title = "Review Taboo Words"
        curStuMsg.content = CONTENT
        curStuMsg.getTime = datetime.now()
        curStuMsg.save()
        
    #check if it has more than 3 complaints
    if curStu.cp_num >= 3:
        curStu.cp_num = curStu.cp_num - 3
        curStu.curStatus = 0

        # add fine to student account
        Ufine = payFine()
        Ufine.sid = curStu.sid
        Ufine.save()
        
    curStu.save()
    curReview.save()
    return render(request, "myadmin/review/curreview.html", {"cur" : curReview})
