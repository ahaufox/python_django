#coding:utf-8
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Threadlist,Threadcheck,Garbage_info


def index(req):
    context={}
    context['nav_id']='index'
    return render(req, 'index.html',context)

def need_do(req):
    context={}
    context['title']='this is title!'
    context['name'] = 'this is name!'
    context['nav_id'] = 'need_do'
    title_list=[]
    insert_time_list=[]
    content_list=[]
    href_list=[]
    username_list=[]
    from_site_list=[]
    for i in Threadlist.objects.all():
    #     title_list.append(i.title)
    #     content_list.append(i.content)
    #     href_list.append(i.href)
    #     username_list.append(i.username)
    #     from_site_list.append(i.from_site)
    #     insert_time_list.append(i.insert_time)
    # context['title_list'] = title_list
    # context['content_list'] = title_list
    # context['href_list'] = title_list
    # context['username_list'] = title_list
    # context['from_site_list'] = title_list
    # context['insert_time_list'] = title_list
        title_list.append([i.title,i.content,i.href,i.from_site,i.username,i.insert_time])
    context['title_list']=title_list
    return render(req,'need_do.html',context)

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

