from django.conf.urls import url

from userApp import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url('^checkname/', views.checkname),
    url(r'activeUser/', views.activeUser),
    url(r'^active/', views.active, name='Active'),
    url(r'get_code/', views.get_code, name='get_code')
]