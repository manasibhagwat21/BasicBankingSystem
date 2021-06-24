from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

app_name='bank'
urlpatterns = [
    #  path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^transfer/', views.transfer, name='transfer'),
    url(r'^userList/', views.userList, name='userList'),
]
