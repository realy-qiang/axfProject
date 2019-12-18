from django.conf.urls import url

from marketApp import views

urlpatterns = [
    url(r'^market/', views.market, name='market'),
]