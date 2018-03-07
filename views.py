
import pymysql
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .control import load_s_config

# Create your views here.


def post_list(request):
    return render(request, 'system911/post_list.html', {})

# def home(request):
# 	sql='select * from `test`;'
# 	a.execute(sql)

# 	countrow = a.execute(sql)
# 	print("Number of rows", countrow)
# 	data = a.fetchall()
# 	print(data)
#     return render(request, 'home.html', {'timeTaken': timetaken})

# def home(request):
#     args = {}
#     sql='select test1,test2 from test;'
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     args['result'] = result

#     return render(request, 'system911/home.html', {'result' : result})



def home(request):
	s_config = load_s_config()
	return render(request, 'system911/home.html',s_config)

def login(request):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"],s_config["port"],s_config["user"], s_config["password"], s_config["database"])
	a=connection.cursor()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		cursor = connection.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT username, password,role FROM user where username='"+username+"' AND password ='"+password+"'")
		result_set = cursor.fetchone()
		
		if result_set :
			#request.session['role'] = "asd"
			if result_set["role"] =='CallOp' :
				#return render(request,'system911/opmenu.html', {'result' : username,"password" : password})
				connection.close()
				return redirect('../opmenu.html');
			else :
				connection.close()
				return render(request,'system911/tst.html', {'result' : username,"password" : password})
		else :
			connection.close()
			return render(request,'system911/home.html',{'fail' : "fail"})

def server_config(request):
	return render(request, 'system911/server_config.html',s_config)
			
def createReport(request):
	return render(request, 'system911/createReport.html', {})

def insertReport(request):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["port"], s_config["user"], s_config["password"], s_config["database"])
	a=connection.cursor()
	if request.method == 'POST':
		incident = request.POST.get('incident')
		cno = request.POST.get('cno')
		rdate = request.POST.get('rdate')
		rtime = request.POST.get('rtime')
		print("Date: " + rdate + " Time: "+ rtime)	
		callerName = request.POST.get('callerName')
		callerContact = request.POST.get('callerContact')	
		location = request.POST.get('location')
		happened = request.POST.get('happened')
		casualties = request.POST.get('casualties')	
		danger = request.POST.get('danger')
		involve = request.POST.get('involve')
		emergencyType = request.POST.get('emergencyType')
		cursor = connection.cursor(pymysql.cursors.DictCursor)
		sql = "INSERT INTO report(`incident`, `date`, `time`, `callerName`, `callerContact`, `location`, `whathappen`, `casualities`, `dangers`, `involvement`, `TypeOfEmergency`) values('"+incident+"','"+rdate+"','"+rtime+"','"+callerName+"','"+callerContact+"','"+location+"','"+happened+"','"+casualties+"','"+danger+"','"+involve+"','"+emergencyType+"')"
		print(sql)
		cursor.execute(sql)
		#INSERT INTO `cnberdynedb`.`report` (`incident`, `caseNumber`, `date`, `time`, `callerInfo`, `callerName`, `callerContact`, `location`, `whathappen`, `casualities`, `dangers`, `involvement`, `typeOfEmergency`) VALUES ('traffic accident', '1', '2018-03-04', '14:14', 'asd', 'asd', '12345678', 'asd', 'd', 'asd', 'asd', 'asd', 'ad');
		connection.commit()
		connection.close()


	return render(request, 'system911/createReport.html', {})

def opmenu(request):


	return render(request, 'system911/opmenu.html', {})
