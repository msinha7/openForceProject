from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^mainpage$', views.mainpage, name='mainpage'),
    url(r'^saveDB$', views.saveDB, name='saveDB'),
    url(r'^getRatingsDB$', views.getRatingsDB, name='getRatingsDB'),
]
