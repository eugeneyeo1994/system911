from django.conf.urls import url
from . import views, control

urlpatterns = [
    url(r'system911/post_list.html', views.post_list, name='post_list'),
    url(r'system911/home.html', views.home, name='home'),
    url(r'system911/login/', views.login, name='login'),

    #call Operator setup
    url(r'system911/createReport.html', views.createReport, name='createReport'),
    url(r'system911/createReport/', views.insertReport, name='insertReport'),
    url(r'system911/opmenu.html', views.opmenu, name='opmenu'),
	url(r'system911/server_config.html', control.go_server_config, name = "server_config"),
	
	url(r'update_server_settings', control.update_server_settings, name = "update_s_settings"),

    #Call TeaLead setup
    url(r'system911/ctmenu.html', views.ctmenu, name='ctmenu'),
    url(r'system911/viewReports.html', views.viewReports, name='viewReports'),
    url(r'system911/updateReport/', views.updateReport, name='updateReport'),

    #supervisor setup
    url(r'system911/supmenu.html', views.supmenu, name='supmenu'),
    url(r'system911/createCases.html', views.createCases, name='createCases'),
    url(r'system911/data.html', views.data, name='data'),
    url(r'system911/makecase', views.makecase, name='makecase'),


    #officer setup
        url(r'system911/officermenu.html', views.officermenu, name='officermenu'),
        url(r'system911/viewCases.html', views.viewCases, name='viewCases'),
        url(r'system911/viewReport2.html', views.viewReport2, name='viewReport2'), #testing
        url(r'system911/updateCase', views.updateCase, name='updateCase'),

    #logout
         url(r'system911/logout', views.logout, name='logout'),
]