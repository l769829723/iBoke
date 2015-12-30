"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from myblog import views
import validation.views
import userinfo.views

# myblog
urlpatterns = [
               url('^$', views.index, name='index'),
]

# validation
urlpatterns += [
                url('^userauth/login/$', validation.views.login, name='login'),
                url('^userauth/register/$', validation.views.register, name='register'),
                url('^userauth/logoff$', validation.views.logoff, name='logoff'),
]

# userinfomations
urlpatterns += [
               url('^userinfo/$', userinfo.views.userinfo, name='userinfo'),
               url('^userinfo/add/$', userinfo.views.publish, name='publish'),
               url('^userinfo/update/$', userinfo.views.update, name='update'),
               url('^userinfo/delete/$', userinfo.views.delete, name='delete'),
]

