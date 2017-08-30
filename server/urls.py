from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth$', views.auth, name='auth'),
    url(r'^viewchats$', views.viewchats, name='viewchats'),
    url(r'^viewchat/(?P<user>[\w|\W]+)/$', views.viewchat, name='viewchat'),
    url(r'^sendmessage/(?P<user>[\w|\W]+)/$', views.sendmessage, name='sendmessage'),
]
