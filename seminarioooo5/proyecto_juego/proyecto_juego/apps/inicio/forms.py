from django.forms import MedelForm
from django import forms
from models import *
class usuarioform(MedelForm):
	class Meta:
		model=usuario