from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import mascota



class listar_mascota(ListView):
	model = mascota
	template_name = 'mascota/listar.html'
listar_mascota = listar_mascota.as_view()


class crear_mascota(CreateView):
	model = mascota
	template_name='mascota/crear.html'
	fields=['dueno','raza','color','sexo','descripcion','perdido','recompenza','foto']
	success_url= reverse_lazy('listar')

crear_mascota=crear_mascota.as_view()	
