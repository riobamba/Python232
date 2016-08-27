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

class Estado232(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='Estacion232')
    valor = models.FloatField()
    fecha = models.DateTimeField()
    servidor = models.TextField()
    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '{}{}'.format(self.fecha, self.valor)

class Estado13(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='Estacion13')
    valor = models.FloatField()
    fecha = models.DateTimeField()
    servidor = models.TextField()
    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '{}{}'.format(self.fecha, self.valor)

class Historial(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='Historial')
    valor = models.FloatField()
    fecha = models.DateTimeField()
    servidor = models.TextField()
    
    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '{}{}'.format(self.fecha, self.valor)


class Funcionamiento(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='funcionamiento')
    valor = models.FloatField()
    fecha = models.DateTimeField()
    servidor = models.TextField()

    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '%s: %s' % (self.fecha, self.valor)


class Funcionamiento_temp(models.Model):
    estacion = models.ForeignKey(Estacion, related_name='funcionamiento_temp')
    valor = models.FloatField()
    fecha = models.DateTimeField()
    servidor = models.TextField()

    class Meta:
        unique_together = ('estacion', 'fecha')
        ordering = ['fecha']

    def __unicode__(self):
        return '%s: %s' % (self.fecha, self.valor)