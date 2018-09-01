
from django.contrib import admin

from .models import Threadlist,Threadcheck,Garbage_info

admin.site.register(Threadlist)
admin.site.register(Garbage_info)
admin.site.register(Threadcheck)