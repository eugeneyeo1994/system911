
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.views.decorators.csrf import csrf_exempt
import json
from .dao import *
# Create your views here.


@csrf_exempt
def receiveCase(request):
	if request.method == 'POST':
		data= request.POST.get('file')
		file = json.loads(data)
		print(file)
	return HttpResponse("received")