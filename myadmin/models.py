from django.db import models
from datetime import datetime

#admin Account model
class adminManagement(models.Model):
    username = models.CharField(max_length=8, primary_key=True)
    pw = models.CharField(max_length=12)
    adminName = models.CharField(max_length=36)

    def toDict(self):
        return {'username':self.username, 'password':self.pw, 'adminName':self.adminName}

    class Meta:
        db_table = "adminManagement"

#Student Model
class student(models.Model):
    sid = models.BigIntegerField(primary_key=True)
    stuName = models.CharField(max_length=36)
    username = models.CharField(max_length=8)
    pw = models.CharField(max_length=12, auto_created='123456')
    gender = models.CharField(max_length=1)
    GPA = models.FloatField(default=0.0)
    email = models.CharField(max_length=64)
    cp_num = models.IntegerField(default=0)
    class_taking = models.IntegerField(default=0)
    class_taken = models.IntegerField(default=0)
    curStatus = models.IntegerField(default=0)

    def toDict(self):
        return {'sid':self.sid, 'username':self.username, 'password':self.pw, 'stuName':self.stuName}

    class Meta:
        db_table = "student"

#Instructor Model
class instructor(models.Model):
    iid = models.BigIntegerField(primary_key=True)
    insName = models.CharField(max_length=36)
    username = models.CharField(max_length=8)
    pw = models.CharField(max_length=12, auto_created='123456')
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=64)
    cp_num = models.IntegerField(default=0)
    class_teaching = models.IntegerField(default=0)
    curStatus = models.IntegerField(default=0)

    def toDict(self):
        return {'iid':self.iid, 'username':self.username, 'password':self.pw, 'insName':self.insName}

    class Meta:
        db_table = "instructor"


#Student Application Model
class stuApplication(models.Model):
    stateid = models.IntegerField(primary_key=True)
    stuName = models.CharField(max_length=36)
    gender = models.CharField(max_length=1)
    GPA = models.FloatField(default=0.0)
    email = models.CharField(max_length=64)
    curStatus = models.SmallIntegerField(default=0)
    info = models.CharField(max_length=36, default="None")
    feedback = models.CharField(max_length=36, default="None")

    class Meta:
        db_table = "stuApplication"


#Instructor Application Model
class insApplication(models.Model):
    stateid = models.IntegerField(primary_key=True)
    insName = models.CharField(max_length=36)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=64)
    curStatus = models.SmallIntegerField(default=0)
    info = models.CharField(max_length=36, default="None")
    feedback = models.CharField(max_length=36, default="None")

    class Meta:
        db_table = "insApplication"

#Course Model
class course(models.Model):
    cid = models.IntegerField(primary_key=True)
    className = models.CharField(max_length=36)
    pre_req = models.IntegerField(default = 0)
    department = models.CharField(max_length=36)

    class Meta:
        db_table = "course"

#Schedules Model
class schedules(models.Model):
    sectionNum = models.IntegerField(primary_key=True)
    className = models.CharField(max_length=36)
    year = models.IntegerField(default=0)
    semester = models.CharField(max_length=36)
    iid = models.IntegerField(default=0)
    days = models.CharField(max_length=10)
    start_time = models.CharField(max_length=20)
    max_limit = models.SmallIntegerField(default=10)
    current_enroll = models.SmallIntegerField(default=0)
    wait_list = models.SmallIntegerField(default=0)
    status = models.CharField(max_length = 10,default='Close')
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = "schedules"

#Student course model
class stuCourse(models.Model):
    sid= models.IntegerField(default = 0)
    cid = models.IntegerField(default = 0)
    sectionNum = models.IntegerField(default = 0)
    year = models.IntegerField(default=0)
    semester = models.CharField(max_length=36)
    grade = models.CharField(max_length=1)
    curStatus = models.IntegerField(default = 2)

    class Meta:
        db_table = "stucourse"

# wait list model
class waitList(models.Model):
    sid= models.IntegerField(default = 0)
    year = models.IntegerField(default=0)
    semester = models.CharField(max_length=36)
    sectionNum = models.IntegerField(default = 0)
    position = models.IntegerField(default = 0)

    class Meta:
        db_table = "waitList"

#complain table model
class complainmsg(models.Model):
    sendType = models.CharField(max_length = 36)
    fromId = models.IntegerField(default = 0)
    fromName = models.CharField(max_length = 36)
    receiveType  = models.CharField(max_length = 36)
    receiveId = models.IntegerField(default = 0)
    receiveName = models.CharField(max_length = 36)
    description = models.CharField(max_length = 1000)
    curStatus  = models.IntegerField(default = 0)
    createdTime = models.DateTimeField(default = datetime.now)

    class Meta:
        db_table = "complainmsg"
        
#Period model
class period(models.Model):
    pid = models.IntegerField(primary_key=True)
    term = models.CharField(max_length=12)
    curPeriod = models.IntegerField(default=0)
    curStatus = models.IntegerField(default=0)
    
    class Meta:
        db_table = "period"
        
#Student Message Model
class stuMsg(models.Model):
    nid = models.IntegerField(primary_key=True)
    receiverID = models.IntegerField(default=0)
    sender = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    getTime = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(default = 0)
    
    class Meta:
        db_table = "stuMsg"

#Instructor Message Model
class insMsg(models.Model):
    nid = models.IntegerField(primary_key=True)
    receiverID = models.IntegerField(default=0)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    getTime = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table = "insMsg"

#Studeng review table
class review(models.Model):
    rid = models.IntegerField(primary_key=True)
    sid = models.IntegerField(default = 0)
    sectionNum = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    content = models.CharField(max_length=256)
    createdTime = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table = "review"

class payFine(models.Model):
    fid = models.IntegerField(primary_key=True)
    sid = models.IntegerField(default = 0)
    amount = models.FloatField(default = 100.00)
    paid = models.FloatField(default = 0)
    status = models.IntegerField(default = 0)
    updateTime = models.DateTimeField(default = datetime.now)

    class Meta:
        db_table = "payFine"