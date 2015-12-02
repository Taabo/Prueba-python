#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from raza.models import raza
from usuario.models import usuario
from models import *
class mascota (models.Model):
	dueno= models.ForeignKey(usuario)
	raza = models.ForeignKey(raza)
	color = models.CharField(max_length=20)
	sexo = models.CharField(max_length=20)
	foto = models.FileField(upload_to = 'mascota')
	descripcion= models.TextField(blank=True, null=True)
	perdido = models.BooleanField(default=False, blank= True)
	recompenza= models.IntegerField(blank=True, null=True,default=0)


	def __str__(self):
		return '%s %s %s' % (self.raza,self.color,self.sexo)