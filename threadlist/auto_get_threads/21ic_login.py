#coding:utf-8
from bs4 import BeautifulSoup
import requests
import cookiejar



# url='http://bbs.21ic.com/home.php?mod=space&do=home&view=all&order=dateline&page=2'
#
# s=requests.get(url).content
# soup=BeautifulSoup(s, "html.parser")
# soup1=soup.select('#feed_div > div > dl > dd > ul > li > div > a:nth-of-type(2)')
# soup2=soup.select('div > h4')
# #soup2=soup.select('#feed_div > div > dl > dd > ul > li > div > span')
# soup3=soup.select('.ec > p > a')
# # for i in soup1:
# #     print(i.get('href'))
# print(soup1)
# print(soup2)
# print(soup3)
url='http://bbs.21ic.com/member.php'
# data={'username':'韦天王',
#       'password':'doushi123888',
#       'quickforward':'yes',
#       'handlekey':'ls'}
# res=requests.session().get(url=url,params=data).cookies._cookies['.21ic.com']['/']
#
# url2='http://bbs.21ic.com/home.php?mod=space'
# print((res))
def LoginByPost(url):
      s=requests.session()
      loginUrl='http://***/admin_loginCheck.php'
      postData={'mod':'logging',
                'action':'login',
                'loginsubmit':'yes',
                'infloat':'yes',
                'lssubmit':'yes',
                'inajax':'1',
                'username':'韦天王',
                'password':'doushi123888',
                'quickforward':'yes',
                'handlekey':'ls'}
      #rs=s.post(loginUrl,postData)
      #url = 'http://bbs.21ic.com/home.php?mod=space'
      res=s.post(loginUrl,postData)
      res.encoding='utf-8'
      print(res.text)
print(LoginByPost(url))