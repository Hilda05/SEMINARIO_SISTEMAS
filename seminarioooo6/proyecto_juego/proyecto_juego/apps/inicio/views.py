from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime
from .models import *

# Create your views here.
def hola(request):
	return render_to_response("base.html",RequestContext(request))
def hola1(request):
	return render_to_response("base1.html",RequestContext(request))
def registro_usuarios(request):
	if request.method=="POST":
		formulario=UserCreation(request.POST)
		if(formulario.is_valid()):
			formulario.save()
			return HttpResponseRedirect("//")

		formulario=UserCreationForm()
		return render_to_response("usuario/registr.html",{'formulario':formulario},context_instance=RequestContext)
def registrou(request):
	if request.method=='POST':
		formulario=usuarioform(request.POST)
		if formulario.is_valid:
			formulario.save()
	else:
		formulario=usuarioform()

	return render_to_response('usuario/reg.html',{'formulario',formulario},RequestContext(request)
		)

	
