from django.conf.urls import url
from . import views, control

urlpatterns = [

	#TEST-receive case
	url(r'systemCMO/receiveCase', views.receiveCase, name='receivecase'),
]