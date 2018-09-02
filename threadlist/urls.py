from . import views
from threadlist import views as view2
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('index.html', views.index, name='index'),
    path('need_do.html',views.need_do),
    path('table_basic.html',views.table_basic),
    path('list', views.list),
    path('login',views.login,name='login')
]
