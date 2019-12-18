from django.conf.urls import url

from cartApp import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    # url(r'checkTotal/', views.checkTotal, name='checkTotal'),
    # url(r'^check/', views.check, name='check'),
    # 添加到购物车
    url(r'^addToCart/', views.addToCart, name='addToCart'),
    # 移出购物车
    url(r'^subToCart/', views.subToCart, name='subToCart'),
    # 修改选中状态
    url(r'^changeCheck/', views.changeCheck, name='changeCheck'),
    # 全选
    url(r'^changeAllCheck/', views.changeAllCheck, name='changeCheck')
]
