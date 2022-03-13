from . import views
from django.urls import path,include
app_name='app'

urlpatterns = [
    path('', views.登陆),
    path('login.html',views.登陆,name='登陆'),
    path('login2.html', views.登陆1, name='登陆'),
    path('love.html',views.登陆),
    path('future.html',views.future,name='future'),
    path('finished.html',views.finished,name='finished'),
    path('information.html',views.information,name='information'),
    path('tables.html',views.tables,name='tables'),
    path('yuding.html',views.yuding,name='yuding'),
    path('index.html',views.index,name='index'),
    path('test.html', views.list, name='list'),
    path('admin.html', views.admin, name='admin'),
    path('addDepart.html', views.addDepart, name='addDepart'),
    path('addDepart1.html', views.addDepart1, name='addDepart1'),
    path('addDepart.html/', views.addDepart),
    path('addDepart1.html/', views.addDepart1),
    path('addroom.html', views.addroom, name='addroom'),
    path('addroom1.html', views.addroom1, name='addroom'),
    path('addUser.html', views.addUser, name='addUser'),
    path('adminmain.html', views.adminmain, name='adminmain'),
    path('correspond.html', views.correspond, name='correspond'),
    path('depart.html', views.depart, name='depart'),
    path('depart1.html', views.depart),
    path('meetingroom.html', views.meetingroom1, name='meetingroom'),
    path('updatePwd.html', views.updatePwd, name='updatePwd'),
    path('user.html', views.user, name='user'),
    path('role/addroleSubmit.action',views.list),
    path('addUser1.html',views.addUser1, name='addUser1'),
    path('cansavelocal.html',views.cans,name='cnas'),
    path('first.html', views.first),
    path('addDetail.html',views.detail),
    path('qianduan.html',views.qianduan),
    path('qianduanyuding.html',views.qdyuding),




]
