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


class Threadcheck(models.Model):
    have_check = models.ForeignKey(Threadlist, on_delete=models.CASCADE)
    check_time = models.DateTimeField('date published')

class Garbage_info(models.Model):
    key_type = models.IntegerField(default=0)#0表示没有问题
    key_value = models.CharField(max_length=200)