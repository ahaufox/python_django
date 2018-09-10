from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('index.html', views.index),
    path('login',views.dlogin,name='login'),
    path('logout', views.do_logout),
    path('pages',views.pages),
    path('register', views.register, name='register'),
    path('message',views.user_message,name='register'),
    path('vuser',views.get_fae_message,name='register')
]
