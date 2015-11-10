from django.db import models
from django.contrib.auth.models import User
from models import *
# Create your models here.
class raza (models.Model):
	tipo = models.CharField(max_length=30,blank=True)


	def __unicode__(self):
		return self.tipo