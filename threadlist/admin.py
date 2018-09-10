from django.contrib import admin

from .models import Threadlist,Messagelist

admin.site.register(Threadlist)
admin.site.register(Messagelist)