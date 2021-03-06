# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import time
import pymysql
import sqlite3
import os
#from PyV8 import JSContext
import re


def get_rel_url(js):
    js = js[31:-9]
    js = 'location = function(){return "http://bbs.21ic.com/icview-2545904-1-1.html\";};' + js
    js = 'window = function(){return \"bbs.21ic.com\";};' + js
    for st in ['window', '\'location\'', '\'assign\'', '\'href\'', '\'replace\'']:
        equal = re.findall('[_A-Za-z0-9= ]+{};'.format(st), js)  # 找到变量赋值等式
        if equal == []:
            continue
        else:
            var = equal[0].split('=')
            left = var[0].strip()
            ri = var[1].strip()
            js = js.replace(left + ';', ri)
            js = js.replace("['{}']".format(st).strip("'"), '.{}'.format(st).strip("'"))
            if re.findall('window.href=\"http://www.php1.cn/\">', js):
                js = js.replace('window.href=\"http://www.php1.cn/\">', js)
                js = js.replace('location.href=\"http://www.php1.cn/\">', js)
    ctxt = JSContext()
    ctxt.__enter__()
    x = (ctxt.eval(js))
    vars = ctxt.locals
    url = 'http://bbs.21ic.com' + str(vars.location['href'])
    return url

def get_text(text):
    text=re.sub('\n','',text)
    text = re.sub('<[^>]+>', '', text)
    return text

def get_threads_21ic(page):
    url = 'http://bbs.21ic.com/forum.php?mod=guide&view=newthread'
    a='&page='
    url=url+a+str(page)
    r=[]
    from_site='21IC'#来源网站
    request = requests.get(url=url).content
    soup = BeautifulSoup(request, "html.parser")
    res=soup.select('tbody > tr > th > a')
    list=len(res)
    for i in range(0,list):
        href = res[i].get('href')
        s = sql_select('select * from threadlist_threadlist where href=\'{}\''.format(href))
        if s:
            pass
        else:
            pub_time_all = soup.select('tbody > tr > td:nth-of-type(3) > em > span')
            user_name_all = soup.select('tbody > tr > td:nth-of-type(3) > cite ')
            c_url = requests.get(url=res[i].get('href')).content
            c_soup = BeautifulSoup(c_url, 'html.parser')
            pub_time = pub_time_all[i].getText()  # 发布时间
            title = get_text(soup.select('tbody > tr > th > a')[i].getText())   # 帖子标题
            user_name = get_text(user_name_all[i].getText())   # 发帖人昵称
            try:
                content = get_text((c_soup.select('.t_f')[0]).text)# 帖子内容
            except:
                c_url=get_rel_url(c_soup.contents)
                c_soup = BeautifulSoup(c_url, 'html.parser')
                content = (c_soup.select('.t_f')[0]).text.encode('utf-8') # 帖子内容
            r.append((from_site, href, pub_time, title, user_name, content))
            insert_to_sql="""insert into threadlist_threadlist (from_site,href,insert_time,title,username,content) values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')""".format(from_site, href, pub_time, title, user_name, content)
            #print(insert_to_sql)
            print(sql_insert(insert_to_sql))
    return url


def sql_insert(sql):
    conn = pymysql.connect("47.105.116.213", "root", "123456", "fae_tool", charset='utf8')
    cursor = conn.cursor()
    try:
        s=cursor.execute(sql)
        ss=conn.commit()
        conn.close()
    except:
        return 'sql错误'
    return 200

def sql_select(sql):
    ss=[]
    conn = pymysql.connect("47.105.116.213", "root", "123456", "fae_tool", charset='utf8')
    cursor = conn.cursor()
    c=cursor.execute(sql)
    s=cursor.fetchall()
    for i in s:
        ss.append(i)
    return ss


print(get_threads_21ic(1))
