"""myweb URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from weibo import views
import sys
# sys.path.append("..")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index,name="index"),
    # url(r'^map/', views.map),
    # url(r'^linechart/',views.linechart),
    # url(r'^debug/',views.debug),
    # url(r'^test/',views.index),
    # url(r'article/(?P<article_id>[0-9]+)',views.article_page,name='article_page'),
    # url(r'edit',views.edit_page,name='edit_page'),
    # url(r'edit/action',views.edit_action,name='edit_action'),
    url(r'weibo/',include('weibo.urls',namespace='weibo'))
]
