"""Service URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from istakip import views
#(?P<pk>[0-9]+)$
#(?P<slug>[\w-]+)/$,
#-\w
#
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^istakip/', views.IstakipList),
    url(r'^istakip/(?P<kullanici>\w+)/(?P<sifre>\w+)$', views.Istakip_detail),
    url(r'^istakip/start/(?P<kullanici>\w+)/(?P<sifre>\w+)/(?P<id>\w+)$',views.Istakip_Start),
    url(r'^istakip/finish/(?P<kullanici>\w+)/(?P<sifre>\w+)/(?P<id>\w+)$',views.Istakip_Finish),
    url(r'^istakip/pause/(?P<kullanici>\w+)/(?P<sifre>\w+)/(?P<id>\w+)$',views.Istakip_Pause),
    #url(r'^(?P<username>[\w.@+-]+)/(?P<order>\d+)/$', 'appname.views.item_home', name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
