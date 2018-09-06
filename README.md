使用说明

1.1 添加用户
将regedit开放即可 
urls中取消注释，前台可以访问即可，views中无需改动
参考网站：https://docs.djangoproject.com/zh-hans/2.1/topics/auth/default/

1.2 关于数据库
已经设置为mysql数据库，具体设置办法：
1、主目录的_init_.py中加入：
import pymysql
pymysql.install_as_MySQLdb()
2、setting中修改
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'fae_tool',
        'USER': 'root',
        'PASSWORD': 'root',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
    }
}