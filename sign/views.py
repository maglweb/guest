# -*-coding:UTF-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf.urls import include, url


# Create your views here.

# 首页，即登录页
def index(request):
    return render(request, 'index.html')


# 登录相关验证，并设置session相关操作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)  # 登录
            response = HttpResponseRedirect('/event_manage/')  # 将session记录到浏览器
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or passowrd error!'})


# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


# 发布会名称搜索
#@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name__contains=search_name)  #
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一个页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果Page不在范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {'user': username, 'guests': contacts})


# 嘉宾手机号的查询
#@login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get('phone', '')
    guest_list = Guest.objects.filter(phone__contains=search_phone)
    return render(request, 'guest_manage.html', {'user': username, 'guests': guest_list})


# 签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {'event': event})


# 签到操作
def sign_index_action(requset, eid):
    event = get_object_or_404(Event, id=eid)
    phone = requset.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)  # 查询手机号在Guest列表中是否存在，如果不存在则提示用户:phone error
    if not result:
        return render(requset, 'sign_index.html', {'event': event, 'hint': 'phone error'})
    result = Guest.objects.filter(phone=phone, event_id=eid)  # 通过手机号和id查询guest表，如果为空，则说明手机号与发布胡不匹配，返回错误提示
    if not result:
        return render(requset, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:  # 判断嘉宾状态是否已签到
        return render(requset, 'sign_index.html', {'event': event, 'hint': 'user has sign in'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(requset, 'sign_index.html', {'event': event, 'hint': 'sign in success!', 'guest': result})


# 退出
@login_required
def logout(request):
    auth.logout(request)  # 退出系统
    response = HttpResponseRedirect('/index/')
    return response
