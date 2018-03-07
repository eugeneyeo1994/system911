import pymysql, json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


# Create your control methods here.

def load_s_config():
	with open("system911/server_config.json", "r") as file:
		data = file.read()
		return json.loads(data)

def go_server_config(request):
	s_config = load_s_config()
	return render(request, 'system911/server_config.html', s_config)

def update_server_settings(request):
	s_config = load_s_config()

	print(s_config)
	
	qdict = request.POST
	for x in qdict:
                if (qdict[x]) :
                        s_config[x] = qdict[x]
						
	print(s_config)
						
	with open("system911/server_config.json", "w") as file:
		data = json.dumps(s_config)
		file.write(data)	
				
	return go_server_config(request)
	
