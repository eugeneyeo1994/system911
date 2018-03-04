from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'system911/post_list.html', views.post_list, name='post_list'),
    url(r'system911/home.html', views.home, name='home'),
    url(r'system911/login/', views.login, name='login'),
    url(r'system911/createReport.html', views.createReport, name='createReport'),
    url(r'system911/createReport/', views.insertReport, name='insertReport'),
    url(r'system911/opmenu.html', views.opmenu, name='opmenu'),

]