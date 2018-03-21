from .control import load_s_config
import pymysql

def dbauthenticate(username,password):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT username, password,role FROM user where username='"+username+"' AND password ='"+password+"'")
	result_set = cursor.fetchone()
	connection.close()
	if(result_set) :
		return result_set
	else:
		return result_set


def dbcreateReport(incident,cno, rdate, rtime, coords, callerName, callerContact, location, happened, casualties, danger, involve, emergencyType):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "INSERT INTO report(`incident`, `date`, `time`, `callerName`, `callerContact`, `location`,`coords`, `whathappen`, `casualities`, `dangers`, `involvement`, `typeOfEmergency`, `severity`) values('"+incident+"','"+rdate+"','"+rtime+"','"+callerName+"','"+callerContact+"','"+location+"','"+coords+"','"+happened+"','"+casualties+"','"+danger+"','"+involve+"','"+emergencyType+"','0')"
	cursor.execute(sql)
	connection.commit()
	connection.close()
	return 1

def dbgetReport():
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT * from report")
	result = cursor.fetchall()
	connection.close()
	return result

def dbupdateReport(caseId,severity):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql ="update report set severity='"+severity+"' where caseNumber='"+ caseId +"'"
	cursor.execute(sql)
	connection.commit()
	connection.close()

def dbgetNreports():
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT * from report where addToCase ='n'")
	result = cursor.fetchall()
	connection.close()
	return result

def dbupdateAddToCase(caseNumber):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	query = "update report set addToCase='y' where caseNumber='"+caseNumber+"';"
	cursor.execute(query)
	connection.commit()
	connection.close()

def dbcreateCase(reportid):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql ="INSERT INTO casetable( `summary`, `reportId`) VALUES('','"+reportid+"');"	
	cursor.execute(sql)
	connection.commit()
	connection.close()

def dbgetCases():
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT * FROM caseTable")
	cases = cursor.fetchall()
	connection.close()
	return cases

def dbupdatecase(cid,caseSum,caseName):
	s_config = load_s_config()
	connection= pymysql.connect(s_config["host"], s_config["user"], s_config["password"], s_config["database"], int(s_config["port"]))
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	query="UPDATE casetable SET caseName = '"+caseName +"', summary='"+caseSum+ "' WHERE caseId ='"+cid+"'";
	cursor.execute(query)
	connection.commit()
	connection.close()

