from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import UserInfor,meetingroom,meeting,department,staff,sudo
from django.db import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User




# Create your views here.
def 登陆(request):
        if request.method == 'GET':
            return render(request, 'login.html')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['name'] = username
            return redirect("/index.html",{"ll":username})
        else:
            return render(request, 'login.html')


def 登陆1(request):
    if request.method == 'GET':
        return render(request, 'login2.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['name'] = username
        return render(request, "index.html", {"ll": username})
    else:
        return render(request, 'login2.html')

def future(request):
    ll=request.user.username
    temp = staff.objects.filter(user_name=user)
    people_list = meeting.objects.all()
    test=meeting.objects.filter(participant__contains=ll)
    vn = {
        'people_list': people_list,
        'opps': temp,
        'test':test,
    }
    return render(request, "future.html",vn)


def finished(request):

        return render(request, "finished.html")




def information(request):
    if request.method == 'POST':
        ll = request.user.username
        name=request.POST.get('姓名',None)
        password = request.POST.get('password', None)
        user = User.objects.get(username=name)
        user.set_password(password)
        user.save()
        return render(request, "information.html",{"ll":ll})
    else:
        ll = request.user.username
        temp=staff.objects.get(user_name=ll)
        vn = {
            'll':ll,
            'temp': temp,
        }
        return render(request, 'information.html',vn)

def tables(request):
    return render(request, "tables.html")

def yuding(request):
    if request.method == 'POST':
        test= request.POST['theme']
        date1 = request.POST.get('date', None)
        start_time1 = request.POST.get('start', None)
        end_time1 = request.POST.get('end', None)
        people=request.POST.get('people',None)
        num=request.POST.get('num',None)
        id=request.POST.get('id',None)
        user = request.user.username
        str = user + ' ' +  people
        meeting.objects.create(
            theme=test,
            date=date1,
            start_time=start_time1,
            participant=str,
            end_time=end_time1,
            create_name=user,
            room_num=num,
            condition='待审核',
            create_num=id
        )
        return render(request, 'yuding.html')
    else:
        user_1 = request.user.username
        temp = staff.objects.get(user_name=user_1)
        return render(request, 'yuding.html',{"opps":temp})



def index(request):
    if request.method=='GET':
        ll=request.user.username
        temp=meeting.objects.filter(create_name=ll)
        opps=meeting.objects.all()
        qs1 = meeting.objects.filter(participant__contains=ll)
        vn={
            'll':ll,
            'temp':temp,
            'opps':opps,
            'qsl':qs1,
        }
        return render(request, "index.html",vn)
    else:
        return render(request, "index.html")


def list(request):
    #ll=request.user.username
    #people = meeting.objects.filter(sname=ll)
    #bob=staff.objects.filter(sno='1')
    #vn={
     #   'people':people,
      #  'bob':bob
       # }
    #return render(request, 'test.html',vn)
    if request.method=="POST":
        people=request.POST.get('参会人员',None)
        meeting.objects.create(
            participant=people   )
        haha =meeting.objects.all
        return render(request, "test.html",{"people_lisr":haha})
    else:
        return render(request, "test.html")

def admin(request):
    if request.method == 'GET':
        return render(request, 'admin.html')
    username = request.POST.get('user', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    temp=User.objects.get(username=username)
    if temp.is_superuser==1:
        if  user is not None:
            login(request, user)
            request.session['name'] = username
            return render(request, "adminmain.html",{"ll":username})
        else:
            return render(request, 'admin.html')
    else:
        return render(request, 'admin.html')




def addDepart(request):
    if request.method == 'POST':
        name = request.POST.get('departName', None)
        num = request.POST.get('departNum', None)
        department.objects.create(
            depart_name=name,
            depart_num=num,
        )
        return render(request, "addDepart.html")
    else:
        return render(request, 'addDepart.html')

def addDepart1(request):
    if request.method == 'GET':
        return render(request, "addDepart1.html")
    else:
        name = request.POST.get('departName', None)
        obj = department.objects.get(edit_state='modify')
        obj.depart_name = name
        obj.edit_state='true'
        obj.save()
        return render(request, "addDepart1.html")


def addroom(request):
    if request.method=='POST':
        id=request.POST.get('userName',None)
        num=request.POST.get('num',None)
        temp1=request.POST.get('ids1',)
        temp2 = request.POST.get('ids2', )
        temp3 = request.POST.get('ids3', )
        if temp1 ==None:
            temp1=' '
        if temp1 == None:
            temp2= ' '
        if temp1 == None:
            temp3= ' '
        str1 =str(temp1) + ' ' + str(temp2) + ' ' + str(temp3)
        str(str1)
        meetingroom.objects.create(
            room_num=id,
            room_size=num,
            equipment=str1
        )
        return render(request,'addroom.html')
    else:
        return render(request,'addroom.html')

def addroom1(request):
    if request.method=='POST':
        num = request.POST.get('num', None)
        temp1 = request.POST.get('ids1', )
        temp2 = request.POST.get('ids2', )
        temp3 = request.POST.get('ids3', )
        str1 = str(temp1) + ' ' + str(temp2) + ' ' + str(temp3)
        str(str1)
        obj = meetingroom.objects.get(edit_state='modify')
        obj.room_size = num
        obj.equipment = str1
        obj.edit_state = 'true'
        obj.save()
        return render(request, 'addroom1.html')
    else:
        temp=meetingroom.objects.get(edit_state='modify')
        return render(request, 'addroom1.html',{"temp":temp})

def addUser(request):
    if request.method == 'POST':
        name = request.POST.get('userName', None)
        phone = request.POST.get('phone', None)
        wechat = request.POST.get('wechat', None)
        sex = request.POST.get('sex', None)
        if sex == '1':
            sex = '男'
        else:
            sex = '女'
        departid = request.POST.get('departid', None)
        staff.objects.create(
            user_name=name,
            phone_num=phone,
            wx_num=wechat,
            gender=sex,
            depart_name=departid
        )
        return render(request, 'addUser.html')
    else:
        ll=department.objects.all()
        return render(request, 'addUser.html',{"ll":ll})

def correspond(request):
    if request.method=='POST':
        temp=request.POST['ll']
        obj=meeting.objects.get(id=temp)
        obj.edit_state='modify'
        obj.save()
        return render(request, 'correspond.html')
    if request.method=='GET':
        ll=meeting.objects.all()
        return render(request, 'correspond.html',{'ll':ll})

def depart(request):
    if request.method=='POST':
        id = request.POST['test']
        type = request.POST['love']
        content=request.POST['hey']
        if type == 'edit':
            obj = department.objects.get(depart_num=id)
            obj.edit_state = 'modify'
            obj.save()
            return render(request, 'depart.html')
        if type == 'cancel':
            obj = department.objects.get(depart_num=id)
            obj.cancel_state = 'true'
            obj.save()
            return render(request, 'depart.html')
        if type == 'search':
            temp=department.objects.filter(depart_name=content)
            return redirect(request, 'depart.html',{"info_list":temp})
    else:
        department.objects.filter(cancel_state='true').delete()
        info_list = department.objects.all()
        return render(request, 'depart.html',{"info_list": info_list})

def meetingroom1(request):
    if request.method=='POST':
        id = request.POST['ll']
        type = request.POST['uu']
        if type == 'edit':
            obj = meetingroom.objects.get(room_num=id)
            obj.edit_state = 'modify'
            obj.save()
        if type == 'cancel':
            obj = meetingroom.objects.get(room_num=id)
            obj.cancel_state = 'true'
            obj.save()
        return render(request, 'meetingroom.html')
    else:
        meetingroom.objects.filter(cancel_state='true').delete()
        temp=meetingroom.objects.all()
        return render(request, 'meetingroom.html',{"temp":temp})

def adminmain(request):
    ll=request.user.username
    info_list = department.objects.all()
    vn={
        "ll":ll,
        "info_list": info_list
    }
    return render(request, 'adminmain.html', vn)

def updatePwd(request):
    if request.method=='POST':
        ll = request.user.username
        password = request.POST.get('password', None)
        user = User.objects.get(username=ll)
        user.set_password(password)
        user.save()
        return render(request, "updatePwd.html")
    else:
        return render(request, 'updatePwd.html')

def user(request):
    if request.method == 'POST':
        id = request.POST.get('ll',None)
        type = request.POST.get('uu',None)
        if type == 'edit':
            obj = staff.objects.get(sno=id)
            obj.edit_state = 'modify'
            obj.save()
        if type == 'cancel':
            obj = staff.objects.get(sno=id)
            obj.cancel_state = 'true'
            obj.save()
        return render(request, 'user.html')
    else:
        staff.objects.filter(cancel_state='true').delete()
        info = staff.objects.all()
        return render(request, 'user.html', {"info": info})

def addUser1(request):
    if request.method == 'GET':
        ll = department.objects.all()
        return render(request, "addUser1.html",{"ll":ll})
    else:
        name = request.POST.get('userName', None)
        phone = request.POST.get('phone', None)
        wechat = request.POST.get('wechat', None)
        sex = request.POST.get('sex', None)
        if sex == '1':
            sex = '男'
        else:
            sex = '女'
        departid = request.POST.get('departid', None)
        obj = staff.objects.get(edit_state='modify')
        obj.user_name=name
        obj.phone_num=phone
        obj.wx_num=wechat
        obj.gender=sex
        obj.depart_name=departid
        obj.edit_state = 'true'
        obj.save()
        return render(request, "addUser1.html")


def cans(request):
    return render(request,"cansavelocal.html")

def first(request):
    if request.method=='POST':
        temp=request.POST.get('pp',None)
        UserInfor.objects.create(
            username=temp
        )
        return render(request,"first.html")
    else:
        return render(request,"first.html")

def detail(request):
    if request.method=='POST':
        temp=request.POST.get('review',None)
        obj=meeting.objects.get(edit_state='modify')
        obj.condition=temp
        obj.edit_state='true'
        obj.save()
        return render(request,"addDetail.html")
    else:
        return render(request, "addDetail.html")

def qianduan(request):
    return  render(request,'qianduan.html')

def qdyuding(request):
    return  render(request,'qianduanyuding.html')
