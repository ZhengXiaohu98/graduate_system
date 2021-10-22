from django.db import models

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
        return {'username':self.username, 'password':self.pw, 'stuName':self.stuName}

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
        return {'username':self.username, 'password':self.pw, 'insName':self.insName}

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
    iid = models.IntegerField(default=0)
    days = models.CharField(max_length=20)
    start_time = models.SmallIntegerField(default=0)
    duration = models.SmallIntegerField(default=0)
    max_limit = models.SmallIntegerField(default=30)
    current_enroll = models.SmallIntegerField(default=0)
    wait_list = models.SmallIntegerField(default=0)
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = "course"