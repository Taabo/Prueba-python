from django.conf.urls import url
from .import views

urlpatterns= [

	url(r'^listar/$', views.listar_mascota, name='listar'),
	url(r'^crear/$', views.crear_mascota, name='crear'),
	#url(r'^listar_perdidas/$', views.listar_perdidas, name='listar_perdidas'),
	
]