from django.conf.urls import url

from mineApp import views

urlpatterns = [
    url(r'^mine/', views.mine, name='mine'),
    url(r'^loginOut/', views.loginOut, name='loginOut')
]