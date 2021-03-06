"""axf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from axf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homeApp/', include('homeApp.urls', namespace='homeApp')),
    url(r'^marketApp/', include('marketApp.urls', namespace='marketApp')),
    url(r'^cartApp/', include('cartApp.urls', namespace='cartApp')),
    url(r'^mineApp/', include('mineApp.urls', namespace='mineApp')),
    url(r'^userApp/', include('userApp.urls', namespace='userApp')),
    url(r'^orderApp/', include('orderApp.urls', namespace='orderApp')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
