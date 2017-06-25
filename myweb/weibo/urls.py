from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^map/$', views.map,name='map'),
    url(r'^linechart/$',views.linechart,name='linechart'),
    url(r'^page_doing/$',views.page_doing,name='page_doing'),
    url(r'^map/action$',views.map_action,name='map_action'),
    url(r'^linechart/action$',views.linechart_action,name='linechart_action'),


    url(r'^debug/$',views.debug),
    url(r'^test/$',views.index),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
    url(r'^edit/action$',views.edit_action,name='edit_action'),

]