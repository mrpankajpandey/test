from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path(r'^check/(?P<user_id>\d+)/$', views.index1 ),

]



