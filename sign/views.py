#-*-coding:UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest

# Create your views here.

#首页，即登录页
def index(request):
    return render(request,'index.html')

#登录相关验证，并设置session相关操作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)#登录
            response = HttpResponseRedirect('/event_manage/')#将session记录到浏览器
            request.session['user'] = username
            return response
        else:
            return render(request,'index.html',{'error':'username or passowrd error!'})

#发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name) #
    return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required
def logout(request):
