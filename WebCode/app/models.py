from django.db import models

# Create your models here.
class UserInfor(models.Model):
    username = models.TextField(null=False)
    condition=models.CharField(null=False,max_length=20,default='modify')


class meetingroom (models.Model):
    room_num=models.CharField(primary_key=True,max_length=20)
    room_location=models.CharField(null='False',max_length =20)
    room_size =models.CharField(null='False',max_length=20)
    equipment=models.CharField(max_length=20,null=True)
    edit_state = models.CharField(max_length=20, null='False')
    cancel_state = models.CharField(max_length=20, null='False')

class department (models.Model):
    depart_num = models.IntegerField(primary_key=True)
    depart_name =models.CharField(max_length =20,null=True)
    edit_state=models.CharField(max_length=20,null='False')
    cancel_state = models.CharField(max_length=20, null='False')

class  staff(models.Model):
    sno=models.AutoField(primary_key=True)
    user_name =models.CharField(max_length=20,null=True)
    user_num=models.IntegerField(null=True)
    face_id=models.ImageField(max_length=20,null=True,default='s')
    depart_name = models.CharField(max_length=20, null='False')
    gender=models.CharField(max_length=20,null='False')
    phone_num=models.IntegerField(null='False')
    wx_num=models.IntegerField(null='False')
    edit_state=models.CharField(max_length=20,null='False')
    cancel_state=models.CharField(max_length=20,null='False',default='false')

class meeting(models.Model):
    create_name = models.CharField(max_length=20, null='False')
    create_num = models.IntegerField(null='False')
    theme=models.CharField(max_length=20,null='False')
    room_num = models.CharField(null='False',max_length=20)
    date = models.DateField(max_length=20, null='False')
    start_time = models.CharField(max_length=20, null='False')
    end_time = models.CharField(max_length=20, null='False')
    participant=models.CharField(max_length=1000,null='False')
    state=models.CharField(max_length=4000,null='TRUE')
    condition=models.CharField(max_length=20,null='False')
    edit_state = models.CharField(max_length=20, null='False')
    cancel_state = models.CharField(max_length=20, null='False', default='false')

class sudo(models.Model):
    name=models.CharField(max_length=20,null='False')
    state=models.CharField(max_length=20,null='False')