from django import forms
from .models import * 

class ChoferForm(forms.ModelForm):
	class Meta:
		model = Chofer 
		fields = ['img','nombre','apellido_paterno', 'apellido_materno',
		 'placa', 'vehiculo', 'salida', 'destino']

		widgets = {

		}