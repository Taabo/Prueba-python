from django.conf.urls import url
from .import views

urlpatterns= [

	url(r'^listar/$', views.listar_mascota, name='listar'),
	url(r'^crear/$', views.crear_mascota, name='crear'),
	
]