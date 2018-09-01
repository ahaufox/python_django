#coding:utf-8
from PyV8 import JSContext
import re

def get_rel_url(js):
    js = js[31:-9]
    # js=js.replace('location','\"http://bbs.21ic.com/icview-2545904-1-1.html\"')
    js = 'location= function(){return "http://bbs.21ic.com/icview-2545904-1-1.html\";};' + js
    js = 'window = function(){return "bbs.21ic.com";};' + js

    for st in ['window', '\'location\'', '\'assign\'', '\'href\'', '\'replace\'']:
        equal = re.findall('[_A-Za-z0-9= ]+{};'.format(st), js)  # 找到变量赋值等式
        if equal == []:
            continue
        else:
            var = equal[0].split('=')
            left = var[0].strip()
            ri = var[1].strip()
            js = js.replace(left + ';', ri)
            # js = js.replace(equal, st)
            # print(js)
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

print(get_rel_url(js))