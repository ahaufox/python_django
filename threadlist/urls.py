from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('index.html', views.index, name='index'),
    path('need_do.html',views.need_do),
    path('table_basic.html',views.table_basic),
    path('list', views.list),
    path('login',views.do_login,name='do_login'),
    path('logout',views.do_logout)
]
