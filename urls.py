from django.conf.urls import url
from . import views, control

urlpatterns = [
    url(r'system911/home_public.html', views.post_list, name='post_list'),
    url(r'system911/home.html', views.home, name='home'),
    url(r'system911/login/', views.login, name='login'),
	#server config
	url(r'system911/server_config.html', control.go_server_config, name = "server_config"),
	url(r'update_server_settings', control.update_server_settings, name = "update_s_settings"),

    #911 Roles Menu
	url(r'system911/menu.html', views.menu, name='menu'),

	#911 Functions(Create,update,read,etc)
    url(r'system911/createReport.html', views.createReport, name='createReport'),
    url(r'system911/createReport/', views.insertReport, name='insertReport'),
	url(r'system911/reportDetails.html', views.viewReportDetails, name='viewReportDetails'),
    url(r'system911/viewReports.html', views.viewReports, name='viewReports'),
    url(r'system911/updateReport/', views.updateReport, name='updateReport'),
    url(r'system911/updateReportByAjax/', views.updateReportByAjax, name='updateReportByAjax'),
    url(r'system911/updateReportByAjax2/', views.updateReportByAjax2, name='updateReportByAjax2'),

    url(r'system911/createCases.html', views.createCases, name='createCases'),
	url(r'system911/viewCases.html', views.viewCases, name='viewCases'),
	url(r'system911/caseDetails.html', views.viewCaseDetails, name='viewCaseDetails'),
    url(r'system911/updateCase', views.updateCase, name='updateCase'),
    url(r'system911/rejectCases.html', views.rejectCase, name='rejectCase'),
    url(r'system911/addReportsToCase', views.addReportsToCase, name='addReportsToCase'),
    url(r'system911/editCase', views.editCase, name='editCase'),
    url(r'system911/modifyCase.html', views.modifyCase, name='modifyCase'),
	
	url(r'system911/viewReport2.html', views.viewReport2, name='viewReport2'), #testing 
	url(r'system911/data.html', views.data, name='data'),
    url(r'system911/makecase', views.makecase, name='makecase'),
	#Send case
	url(r'system911/sendCase', views.sendCase, name='sendcase'),
	#TEST-receive case
	url(r'system911/receiveCase', views.receiveCase, name='receivecase'),
    #logout
         url(r'system911/logout', views.logout, name='logout'),
]