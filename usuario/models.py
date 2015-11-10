from django.db import models
from django.contrib.auth.models import User
from models import *

class usuario(User):

	telefono = models.PositiveIntegerField()
	direccion = models.TextField()

	def __unicode__(self):
		return self.username



	