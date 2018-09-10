from django.db import models


class Threadlist(models.Model):
    href=models.CharField(default='',max_length=100,null=True)
    content=models.TextField(default='',max_length=999,null=True)
    username = models.CharField(max_length=50,verbose_name='发帖人昵称',null=True)
    title = models.TextField(verbose_name='帖子标题',null=True)
    insert_time = models.DateTimeField(verbose_name='记录到数据库的时间（近似与发帖时间）')
    from_site=models.CharField(null=True,max_length=200)
    def __unicode__(self):
        return self.name

class Messagelist(models.Model):
    from_user=models.CharField(default='',max_length=100,null=True)
    to_user = models.CharField(default='', max_length=100, null=True)
    message_content=models.CharField(default='',max_length=1000, null=True)
    send_time = models.DateTimeField(default='', null=True)
    message_state = models.CharField(default='', max_length=100, null=True)
    def __unicode__(self):
        return self.name