from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'processregistration$', views.registration),
    url(r'logout$', views.logout),
    url(r'login$', views.login),
    url(r'admin$', views.admin),
    url(r'users/(?P<number>[0-9]+)/destroy$', views.delete),
    url(r'postmessage$', views.postmessage),
    url(r'postcomment$', views.postcomment),
    url(r'deletemessage/(?P<number>[0-9]+)$', views.deletemessage),
    url(r'deletecomment/(?P<number>[0-9]+)$', views.deletecomment)
]