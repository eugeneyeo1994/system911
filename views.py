
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.views.decorators.csrf import csrf_exempt
import json
from .dao import *
# Create your views here.


def post_list(request):
    return render(request, 'system911/home_public.html', {})

def home(request):
	s_config = load_s_config()
	return render(request, 'system911/home.html',s_config)

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		result_set = dbauthenticate(username,password)
		print(result_set)
		if result_set :
			
			if result_set["role"] =='CallOp' :
				request.session['role'] = "CallOp"

			if result_set["role"] =='CallCT':
				request.session['role'] = "CallCT"
				
			if result_set["role"] =='sup':
				request.session['role'] = "sup"

			if result_set["role"] =='911officer':
				request.session['role'] = "911officer"
				
			if result_set["role"] =='CMOofficer':
				request.session['role'] = "CMOofficer"
			return redirect('../menu.html');
		else :
			return redirect('../../home.html');
		
		
def createReport(request):
	return render(request, 'system911/createReport.html')

def insertReport(request):
	if request.method == 'POST':
		incident = request.POST.get('incident')
		cno = request.POST.get('cno')
		rdate = request.POST.get('rdate')
		rtime = request.POST.get('rtime')
		coords = request.POST.get('coords')
		print("Date: " + rdate + " Time: "+ rtime)	
		callerName = request.POST.get('callerName')
		callerContact = request.POST.get('callerContact')	
		location = request.POST.get('location')
		happened = request.POST.get('happened')
		casualties = request.POST.get('casualties')	
		danger = request.POST.get('danger')
		involve = request.POST.get('involve')
		emergencyType = request.POST.get('emergencyType')
		test = dbcreateReport(incident,cno, rdate, rtime, coords, callerName, callerContact, location, happened, casualties, danger, involve, emergencyType)
	return render(request, 'system911/createReport.html')

def menu(request):
	if 'role' in request.session:
	    role = request.session['role']
	    if role == "CallOp" :
		    return render(request, 'system911/opmenu.html')
	    if role == "CallCT":
		    return render(request, 'system911/ctmenu.html')
	    if role == "sup":
		    return render(request, 'system911/supmenu.html')
	    if role == "911officer" :
		    return render(request, 'system911/911officermenu.html')
	    if role == "CMOofficer" :
		    return render(request, 'system911/CMOofficermenu.html')
	    
	    return render(request, 'system911/home.html')
	else :
		return render(request, 'system911/home.html')
	#=============================REPORTS==========================
def viewReports(request):
	result = dbgetReport()
	return render(request, 'system911/viewReports.html', {'result' : result})
	
def viewReportDetails(request):
	if request.method == 'GET':
		reportid = request.GET.get('reportid')
		report = dbgetReport() #add id to argument later, 
	return render(request, 'system911/reportDetails.html', {'test':reportid, 'result': report})

def updateReport(request):
	if request.method == 'POST':
		caseId = request.POST.get('cid')
		severity = request.POST.get('severity')
		dbupdateReport(caseId,severity)
	return render(request, 'system911/viewReports.html')

	#=======????======

def data(request):

	return render(request, 'system911/data.html')

	#=============================CASES==========================
def createCases(request):
	result = dbgetNreports()
	return render(request, 'system911/createCases.html', {'result' : result})	
	
#@csrf_exempt
def makecase(request):
	if request.is_ajax() : 
		if request.method == 'POST':
			data = json.loads(request.body.decode('utf-8'))
			print(data)
			createdCaseId = dbcreateCase()
			for d in data["selectedItems"] : 
				 if d["reportId"] :
				 	dbupdateAddToCase(d["reportId"], createdCaseId)
			response_data = {}
			response_data['message'] = 'success'
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def viewCases(request):
	cases = dbgetCases()
	reports = dbgetYreports()
	return render(request, 'system911/viewCases.html', {"cases" : cases, "result" : reports})


def	viewCaseDetails(request):
	if request.method == 'GET':
		caseid = request.GET.get('caseid')
		reports = dbgetReport() #add id to argument later, 
	return render(request, 'system911/caseDetails.html', {'testcase':caseid, 'result': reports})

		
def viewReport2(request):
	reports = dbgetYreports()
	cases = dbgetCases()
	nreports = dbgetNreports()
	#print(nreports)
	return render(request, 'system911/viewReport2.html', {'result' : reports,"cases" : cases, "nreports" : nreports})


def modifyCase(request):
	reports = dbgetYreports()
	cases = dbgetCases()
	nreports = dbgetNreports()
	#print(nreports)
	return render(request, 'system911/modifyCase.html', {'result' : reports,"cases" : cases, "nreports" : nreports})


def updateCase(request):
	if request.method == 'POST' :
		dbupdatecase(cid,caseSum,caseName)
	return render(request, 'system911/home.html')



def addReportsToCase(request):
	if request.is_ajax() : 
		if request.method == 'POST':
			data = json.loads(request.body)
			#print(data["caseid"])
			for d in data["selectedReports"] : 
			 	if d :
			 		dbaddNewReportToCase(d, data["caseid"])	

	reports = dbgetYreports()
	for r in reports :
		r["date"] = str(r["date"])
		r["time"] = str(r["time"])
		
	
	nreports = dbgetNreports()	
	response_data = {}
	response_data['message'] = 'success'
	response_data['reports'] = reports
	for n in nreports :
		n["date"] = str(n["date"])
		n["time"] = str(n["time"])
	response_data['nreports'] = nreports
	print("JSONNNNN:::: "+json.dumps(response_data))
	return HttpResponse(json.dumps(response_data), content_type="application/json")




def rejectCase(request):
	return render(request, 'system911/rejectCases.html')


def logout(request):
	del request.session['role']
	request.session.modified = True
	return render(request, 'system911/home.html')

def editCase(request):
	if request.is_ajax() : 
		if request.method == 'POST':
			data = json.loads(request.body.decode('utf-8'))
			#print(data)
			dbupdatecase(str(data["caseId"]), data["summary"], data["cName"])
			for d in data["reportId"] : 
			 	if d :
			 		print(d)
			 		dbaddNewReportToCase(str(d), "0")
			
	reports = dbgetYreports()
	for r in reports :
		r["date"] = str(r["date"])
		r["time"] = str(r["time"])
		
	cases = dbgetCases()
	nreports = dbgetNreports()	
	response_data = {}
	response_data['message'] = 'success'
	response_data['reports'] = reports
	response_data['cases'] = cases
	for n in nreports :
		n["date"] = str(n["date"])
		n["time"] = str(n["time"])
	response_data['nreports'] = nreports
	print("JSONNNNN:::: "+json.dumps(response_data))
	return HttpResponse(json.dumps(response_data), content_type="application/json")