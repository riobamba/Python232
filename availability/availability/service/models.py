from __future__ import unicode_literals

from django.db import models

class Estacion(models.Model):
    estacion = models.TextField()
    red = models.TextField()
    localizador = models.TextField()
    latitud = models.TextField()
    longitud = models.TextField()
    administrador = models.TextField()
    canal = models.TextField()
    

class Funcionamiento(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='funcionamiento')
    valor = models.TextField()
    fecha = models.DateField()
    
    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '%s: %s' % (self.fecha, self.valor)
