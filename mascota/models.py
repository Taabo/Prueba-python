#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from raza.models import raza
from usuario.models import usuario
from models import *
class mascota (models.Model):
	dueno= models.ForeignKey(usuario)
	raza = models.ForeignKey(raza)
	color = models.CharField(max_length=20, blank=True)
	sexo = models.CharField(max_length=20, blank=True)
	foto = models.FileField(upload_to = 'mascota')
	descripcion= models.TextField(null=True)
	perdido = models.BooleanField()
	recompenza= models.IntegerField(null=True)


	def __str__(self):
		return self.descripcion