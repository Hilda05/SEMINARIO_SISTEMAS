from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime

# Create your views here.
def hola(request):
	return render_to_response("base.html",RequestContext(request))
