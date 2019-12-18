from django.conf.urls import url

from homeApp import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
]