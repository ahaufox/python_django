#coding:utf-8
from django.template import loader
from django.http import HttpResponse
from .models import Threadlist,Messagelist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        context={}
        thread_num=len(Threadlist.objects.all())
        context['nav_id']='index'
        context['thread_num']=thread_num
        return render(request, 'index.html',context)
    else:
        return redirect('login')

def register(request):
    if request.method=='GET':
        return render(request, 'register.html')
    if request.method=='POST':
        username = request._post['name']
        password = request._post['password']
        count = User.objects.filter(username=username)
        if count:
            return HttpResponse('账号已存在')
        else:
            user=User.objects.create_user(username,'',password)
            return redirect('login')

def dlogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request._post['name']
            password = request._post['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')
            else:
                contant={}
                contant['msg']='账号密码不对'
                return render(request, 'login.html', contant)
        else:
            contant = {}
            contant['msg'] = ''
            return render(request, 'login.html', contant)

def do_logout(request):
    logout(request)
    return redirect('login')

def pages(request):
    x=20
    contact_list = Threadlist.objects.all().order_by("id")
    paginator = Paginator(contact_list, x,5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'need_do_page.html', {'contacts': contacts,'nav_id':'pages','page_num':x})

def user_message(request):
    contact_list = Messagelist.objects.all()
    paginator = Paginator(contact_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'message.html', {'contacts': contacts, 'nav_id': 'message_all'})

def get_fae_message(request):
    content={}
    content['res']='True'
    return render(request,'get_fae_message.html',content)

def test_py(request):
    import os
    pathname = os.path.dirname(os.path.abspath(__file__))
    py_dir = pathname + '\\auto_get_threads\\'
    py_name = 'get_thread.py'
    os.system('python ' + py_dir + py_name)

    return  ('python ' + py_dir + py_name)
