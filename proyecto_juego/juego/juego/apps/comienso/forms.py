#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *
import pdb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField


class fcapcha(forms.Form):
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})
class usuarioform(ModelForm):
 	class Meta:
 		model=usuario
class fperfil(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']
class fusuario(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="Contraseña de confirmación", widget=forms.PasswordInput)
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","email")
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user 
class fperfil_modificar(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']

class feditar_perfil(forms.Form):
	email=forms.EmailField(max_length=100,required=True,label="Email")
	#password=forms.CharField(help_text=False,label="Contraseña nueva", widget=forms.PasswordInput)
class feditar_pass(forms.Form):
	password=forms.CharField(help_text=False,label="Contraseña nueva", widget=forms.PasswordInput)




class ftema(ModelForm):
	class Meta:
		model=Tema
class fpregunta(ModelForm):
	nombre=forms.CharField(required=True,label="Pregunta :")
	class Meta:
		model=Pregunta
		exclude=['tema']
class frespuesta(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['pregunta']