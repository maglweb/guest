#-*-coding:UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request,'index.html')


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

def event_manage(request):
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username})