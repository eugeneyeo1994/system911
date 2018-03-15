
import pymysql
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .control import load_s_config

from django.views.decorators.csrf import csrf_exempt
import json
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
	#s_config = load_s_config()
	connection= pymysql.connect(host='35.224.24.23',user='root', password='P@ssw0rd', db='cnberdynedb')
	#a=connection.cursor()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		cursor = connection.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT username, password,role FROM user where username='"+username+"' AND password ='"+password+"'")
		result_set = cursor.fetchone()
		
		if result_set :
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
			
			request.session['role'] = "asd"
>>>>>>> parent of 55e0e6a... latest update
=======
			request.session['role'] = "asd"
>>>>>>> parent of 55e0e6a... latest update
=======
			request.session['role'] = "asd"
>>>>>>> parent of 55e0e6a... latest update
=======
			request.session['role'] = "asd"
>>>>>>> parent of 55e0e6a... latest update
			if result_set["role"] =='CallOp' :
				#return render(request,'system911/opmenu.html', {'result' : username,"password" : password})
				connection.close()

				return redirect('../opmenu.html');

			elif result_set["role"] =='CallCT':
				connection.close()
				return redirect('../ctmenu.html')
				
			elif result_set["role"] =='sup':
				connection.close()
				return redirect('../supmenu.html')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

			elif result_set["role"] =='officer':
				request.session['role'] = "officer"
				connection.close()
				return redirect('../officermenu.html')

=======
				
>>>>>>> parent of 55e0e6a... latest update
=======
				
>>>>>>> parent of 55e0e6a... latest update
=======
				
>>>>>>> parent of 55e0e6a... latest update
			else :
				connection.close()
				return render(request,'system911/tst.html', {'result' : username,"password" : password})
		else :
			connection.close()
			return render(request,'system911/home.html',{'fail' : "fail"})

def server_config(request):
	return render(request, 'system911/server_config.html',s_config)
			
def createReport(request):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	return render(request, 'system911/createReport.html')

def insertReport(request):
	#s_config = load_s_config()
	#connection= pymysql.connect(s_config["host"], s_config["port"], s_config["user"], s_config["password"], s_config["database"])
	connection= pymysql.connect(host='127.0.0.1',user='root', password='password', db='cnberdynedb')

	return render(request, 'system911/createReport.html', {})

def insertReport(request):
=======
	return render(request, 'system911/createReport.html', {})

def insertReport(request):
>>>>>>> parent of 55e0e6a... latest update
=======
	return render(request, 'system911/createReport.html', {})

def insertReport(request):
>>>>>>> parent of 55e0e6a... latest update
=======
	return render(request, 'system911/createReport.html', {})

def insertReport(request):
>>>>>>> parent of 55e0e6a... latest update
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["port"], s_config["user"], s_config["password"], s_config["database"])
	#a=connection.cursor()
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
		sql = "INSERT INTO report(`incident`, `date`, `time`, `callerName`, `callerContact`, `location`, `whathappen`, `casualities`, `dangers`, `involvement`, `typeOfEmergency`, `severity`) values('"+incident+"','"+rdate+"','"+rtime+"','"+callerName+"','"+callerContact+"','"+location+"','"+happened+"','"+casualties+"','"+danger+"','"+involve+"','"+emergencyType+"','0')"
		#print(sql)
		cursor.execute(sql)
		#INSERT INTO `cnberdynedb`.`report` (`incident`, `caseNumber`, `date`, `time`, `callerInfo`, `callerName`, `callerContact`, `location`, `whathappen`, `casualities`, `dangers`, `involvement`, `typeOfEmergency`) VALUES ('traffic accident', '1', '2018-03-04', '14:14', 'asd', 'asd', '12345678', 'asd', 'd', 'asd', 'asd', 'asd', 'ad');
		connection.commit()
		connection.close()


	return render(request, 'system911/createReport.html', {})

def opmenu(request):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	if 'role' in request.session:
	    role = request.session['role']
	    print(role);
	    if role == "CallOp" :
	    	return render(request, 'system911/opmenu.html')
	    elif role == "CallCT":
	    	return render(request, 'system911/ctmenu.html')
	    elif role == "sup":
	    	return render(request, 'system911/supmenu.html')
	    elif role == "officer":
	    	print("reached officer")
	    	return render(request, 'system911/officermenu.html')
	    else:
	    	return render(request, 'system911/home.html')
	else :
		return render(request, 'system911/home.html')

def ctmenu(request):
	if 'role' in request.session:
	    role = request.session['role']
	    print(role);
	    if role == "CallOp" :
	    	return render(request, 'system911/opmenu.html')
	    elif role == "CallCT":
	    	return render(request, 'system911/ctmenu.html')
	    elif role == "sup":
	    	return render(request, 'system911/supmenu.html')
	    elif role == "officer":
	    	print("reached officer")
	    	return render(request, 'system911/officermenu.html')
	    else:
	    	return render(request, 'system911/home.html')
	else :
		return render(request, 'system911/home.html')
	return render(request, 'system911/opmenu.html', {})

def ctmenu(request):
=======


	return render(request, 'system911/opmenu.html', {})

def ctmenu(request):
>>>>>>> parent of 55e0e6a... latest update
=======


	return render(request, 'system911/opmenu.html', {})

def ctmenu(request):
>>>>>>> parent of 55e0e6a... latest update
=======


	return render(request, 'system911/opmenu.html', {})

def ctmenu(request):
>>>>>>> parent of 55e0e6a... latest update


	return render(request, 'system911/ctmenu.html', {})

def viewReports(request):
	connection= pymysql.connect(host='127.0.0.1',user='root', password='password', db='cnberdynedb')
	#a=connection.cursor()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT * from report")
	result = cursor.fetchall()
	connection.close()
	return render(request, 'system911/viewReports.html', {'result' : result})

def viewReport2(request):

	return render(request, 'system911/viewReport2.html')

def updateReport(request):
	connection= pymysql.connect(host='127.0.0.1',user='root', password='password', db='cnberdynedb')
	if request.method == 'POST':
		caseId = request.POST.get('cid')
		severity = request.POST.get('severity')
		cursor = connection.cursor(pymysql.cursors.DictCursor)
		sql ="update report set severity='"+severity+"' where caseNumber='"+ caseId +"'"
		cursor.execute(sql)



		connection.commit()
		connection.close()
		print(severity)
	return render(request, 'system911/viewReports.html')

	
def supmenu(request):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	if 'role' in request.session:
	    role = request.session['role']
	    print(role);
	    if role == "CallOp" :
	    	return render(request, 'system911/opmenu.html')
	    elif role == "CallCT":
	    	return render(request, 'system911/ctmenu.html')
	    elif role == "sup":
	    	return render(request, 'system911/supmenu.html')
	    elif role == "officer":
	    	print("reached officer")
	    	return render(request, 'system911/officermenu.html')
	    else:
	    	return render(request, 'system911/home.html')
	else :
		return render(request, 'system911/home.html')
	return render(request, 'system911/supmenu.html')
>>>>>>> parent of 55e0e6a... latest update
=======

	return render(request, 'system911/supmenu.html')
>>>>>>> parent of 55e0e6a... latest update
=======

	return render(request, 'system911/supmenu.html')
>>>>>>> parent of 55e0e6a... latest update
=======

	return render(request, 'system911/supmenu.html')
>>>>>>> parent of 55e0e6a... latest update

def createCases(request):
	connection= pymysql.connect(host='127.0.0.1',user='root', password='password', db='cnberdynedb')
	#a=connection.cursor()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT * from report where addToCase ='n'")
	result = cursor.fetchall()
	connection.close()
	for row in result:
	     if row["severity"] == 1 : 
	     	row["severity"] = "green.png"
	     	print(row["severity"])

	return render(request, 'system911/createCases.html', {'result' : result})

def data(request):

	return render(request, 'system911/data.html')


# def makecase(request):
# 	if request.method == 'POST':
#         print("asd") print 'Raw Data: "%s"' % request.body   
# return render(request, 'system911/data.html')

#@csrf_exempt
def makecase(request):
	if request.is_ajax() : 
		if request.method == 'POST':
			connection= pymysql.connect(host='127.0.0.1',user='root', password='password', db='cnberdynedb')
			cursor = connection.cursor(pymysql.cursors.DictCursor)
			reportid=""
			data = json.loads(request.body)
			for d in data["selectedItems"] : 
				if reportid =="" :
					reportid = ""+d["CaseNumber"]
				else :
					reportid = reportid+","+d["CaseNumber"]
				query = "update report set addToCase='y' where caseNumber='"+d["CaseNumber"]+"';"
				cursor.execute(query)
				print(query)
			sql ="INSERT INTO casetable( `summary`, `reportId`) VALUES('','"+reportid+"');"	
			print(sql)
			cursor.execute(sql)
			connection.commit()
			connection.close()
			response_data = {}
			response_data['message'] = 'success'
	return HttpResponse(json.dumps(response_data), content_type="application/json")


def officermenu(request):

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def logout(request):
	del request.session['role']
	request.session.modified = True
	return render(request, 'system911/home.html')
	return render(request, 'system911/officermenu.html')
=======
	return render(request, 'system911/officermenu.html')
>>>>>>> parent of 55e0e6a... latest update
=======
	return render(request, 'system911/officermenu.html')
>>>>>>> parent of 55e0e6a... latest update
=======
	return render(request, 'system911/officermenu.html')
>>>>>>> parent of 55e0e6a... latest update
