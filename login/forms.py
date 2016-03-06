from django import forms
from .models import * 

class ChoferForm(forms.ModelForm):
	class Meta:
		model = Chofer 
		fields = ['img','nombre','apellido_paterno', 'apellido_materno',
		 'placa', 'vehiculo', 'salida', 'destino']

		widgets = {
			'nombre': forms.TextInput(
					attrs = {'id':'nombre', 'placeholder':'David', 'required':True }
				),
			'apellido_paterno': forms.TextInput(
					attrs = {'id':'apellido_paterno', 'placeholder':'Cermeño', 'required':True }
				),
			'apellido_materno': forms.TextInput(
					attrs = {'id':'apellido_materno', 'placeholder':'Moranchel', 'required':True }
				),

			'placa': forms.TextInput(
					attrs = {'id':'placa', 'placeholder':'498-XAJ', 'required':True }
				),

			'vehiculo': forms.TextInput(
					attrs = {'id':'vehiculo', 'placeholder':'Vagoneta', 'required':True }
				),

			'salida': forms.TextInput(
					attrs = {'id':'salida', 'placeholder':'El rosario', 'required':True }
				),

			'destino': forms.TextInput(
					attrs = {'id':'destino', 'placeholder':'Chapultepec', 'required':True }
				),

		}



