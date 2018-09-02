#coding:utf-8
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Threadlist,Threadcheck,Garbage_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(req):
    context={}
    thread_num=len(Threadlist.objects.all())
    context['nav_id']='index'
    context['thread_num']=thread_num
    return render(req, 'index.html',context)

def need_do(req):
    context={}
    context['title']='this is title!'
    context['name'] = 'this is name!'
    context['nav_id'] = 'need_do'
    list=[]
    for i in Threadlist.objects.all():
        list.append([i.from_site,i.username,i.insert_time,i.title,i.content,i.href])
    context['list'] = list
    return render(req,'need_do.html',context)
def pages(request):
    context = {}
    list = []
    for i in Threadlist.objects.all():
        list.append([i.from_site,i.username,i.insert_time,i.title,i.content,i.href])
    context['list'] = list
    pages=Paginator(list, 25)
    page = request.GET.get('page')
    try:
        contacts = pages.page(page)
    except PageNotAnInteger:
        contacts = pages.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        contacts = pages.page(pages.num_pages)  # If page is out of range (e.g. 9999), deliver last page of results.
        return render(request, 'need_do.html', {'contacts': contacts})

def table_basic(request):
    context = {}
    context['id']=[1,2,3,4,5,6]
    context['id2'] = [1, 2, 3, 4]
    context['checked'] = 'checked'
    context['nchecked'] = ''
    context['title']= 'this is list title!'
    context['name'] = 'this is name!'
    context['url'] = 'http://bbs.21ic.com/icview-2542950-1-1.html'
    return  render(request,'table_basic.html',context)

def list(request):
    latest_question_list = Threadlist.objects.order_by('insert_time')[:5]
    template = loader.get_template('list.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #title = ', '.join([q.title for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def edit(request,thread_id):
    response = ("edit，对有意向的帖子标记，当前标记的帖子id=%s" % thread_id)
    return HttpResponse(response)

def list_have_edit(request,thread_type):
    return HttpResponse("显示一类已经被标记的帖子详情，type值=%s" % thread_type)

def login(request):
    context={}
    context['name']='myname'
    if request.method=='POST':
        return HttpResponse('ddd')
    else:
        return render(request,'login.html',context)