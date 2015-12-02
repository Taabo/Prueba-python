from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import mascota_perdida


class listar_mascota (ListView):
    model = mascota_perdida
    template_name = 'mascota_perdida/listar.html'

listar_mascota=listar_mascota.as_view()



class update_mascota(UpdateView):
    model = mascota_perdida
    fields= '__all__'
    template_name = 'mascota_perdida/update.html'

update_mascota=update_mascota.as_view()

class delete_mascota(DeleteView):
	model= mascota_perdida
	template_name='mascota_perdida/mascota_perdida_confirm_delete.html'

delete_mascota= delete_mascota.as_view()




# Create your views here.
