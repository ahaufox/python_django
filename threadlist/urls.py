from . import views
from threadlist import views as view2
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('index.html', views.index, name='index'),
    path('need_do.html',views.need_do),
    path('table_basic.html',views.table_basic),
    path('list', views.list),
    path('<int:thread_id>/', views.edit, name='edit'),
    path('edit/<int:thread_type>/',views.list_have_edit,name='list_have_edit'),
]
