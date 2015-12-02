from django.db import models
from raza.models import raza

class mascota_perdida(models.Model):
	raza = models.ForeignKey(raza)
	color = models.CharField(max_length=20, blank=True)
	sexo = models.CharField(max_length=20, blank=True)
	foto = models.FileField(upload_to = 'mascota')
	descripcion= models.TextField(null=True)
	recompenza= models.IntegerField(null=True)
	sector= models.CharField(max_length=40, blank= True)
	direccion= models.CharField(max_length=40)

	def __unicode__(self):
		return self.raza

# Create your models here.
