from django.conf.urls import url
from .import views

urlpatterns= [
	
	url(r'^listar/$', views.listar_mascota, name='listar'),
	url(r'^update/(?P<pk>\d+)/$', views.update_mascota, name='update'),
	url(r'^delete/(?P<pk>\d+)/$', views.delete_mascota, name='delete'),


]