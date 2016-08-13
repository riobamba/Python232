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
    def __unicode__(self):
        return '{}'.format(self.estacion)

class Estado(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='Estado')
    valor = models.TextField()
    fecha = models.DateTimeField()
    
    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '{}{}'.format(self.fecha, self.valor)

class Historial(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='Historial')
    valor = models.TextField()
    fecha = models.DateTimeField()
    
    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '{}{}'.format(self.fecha, self.valor)
