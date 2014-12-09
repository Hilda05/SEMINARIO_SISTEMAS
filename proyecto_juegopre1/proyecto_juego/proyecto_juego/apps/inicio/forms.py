from django.forms import ModelForm
from django import forms
from models import * 
class usuarioform(ModelForm):
 	class Meta:
 		model=usuario
