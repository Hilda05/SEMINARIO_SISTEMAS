from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb
from forms import *


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

	return render_to_response('usuario/reg.html',{'formulario',formulario},RequestContext(request))
	#datos=usuario.objects.all()	
	#return render_to_response ('base.html',RequestContext(request))
	#return render_to_response("usuario/reg.html",{'datos',datos},context_instance=RequestContext(request))

def ingresar(request):
	if render_to_response.method=='POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/home')
				else: 
					return render_to_response('usuario/noactivo.html',context_instance=RequestContext(request))
			else:
				return render_to_response('usuario/nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('usuario/ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))

#pagina de inicio del sistema

	
