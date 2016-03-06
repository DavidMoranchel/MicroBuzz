from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy #para regresar a otra url
from django.views.generic import ListView, DetailView #vistas para lista y detalle
from django.views.generic.edit import CreateView, UpdateView, DeleteView #vistas para modificar
from .models import Chofer, Usuario #importamos el modelo]
from .forms import * 




def base(request):
	c = Chofer.objects.all()


	if request.method == 'POST':
		print('ok POST')
		cForm = ChoferForm(request.POST)

		if cForm.is_valid():
			cForm.save()

		else:
			return render(request, 'chofer.html',{'chofer':c, 'form':ChoferForm(request.POST)})
	#a = Aerolinea.objects.all()


	return render(request,'chofer.html', {'chofer':c, 'form':ChoferForm()})