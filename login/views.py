from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy #para regresar a otra url
from django.views.generic import ListView, DetailView #vistas para lista y detalle
from django.views.generic.edit import CreateView, UpdateView, DeleteView #vistas para modificar
from .models import Chofer, Usuario #importamos el modelo



listaChofer = ['img', 'nombre', 'apellido_paterno','apellido_materno','placa','vehiculo',
				'salida', 'destino'] #Lista de los campos para no repetir

#Lista de todas las tienda
class ChoferListView(ListView):
    model = Chofer #Con esto jala todo el modelo
    template_name = "index.html" #le decimos que template tiene que hacer el response

class ChoferDetail(DetailView):
	model = Chofer #con esto jala todo el modelo
	def get_context_data(self, **kwargs):
	    context = super(ChoferDetail, self).get_context_data(**kwargs)
	    return context #aqui regresa el resultado de la tienda solicitada

class ChoferCreate(CreateView):
	model = Chofer
	fields = listaChofer
	success_url = reverse_lazy('home') #con reverse_lazy le decimos que nos redirecciones cuando guarde el registro

class ChoferUpdate(UpdateView):
	model = Chofer
	fields = listaChofer
	success_url = reverse_lazy('home')

class ChoferDelete(DeleteView):
	model = Chofer
	success_url = reverse_lazy('home')