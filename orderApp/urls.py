from django.conf.urls import url

from orderApp import views

urlpatterns = [
    url(r'^order/', views.order, name='order'),
    url(r'^order_detail/', views.order_detail, name='order_detail'),
    url(r'^testPay/', views.testPay, name='testPay')
]