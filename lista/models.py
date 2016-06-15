# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Participante(models.Model):
	class Meta:
		verbose_name_plural = 'Participantes'
		verbose_name = 'Participante'

	nome = models.CharField(verbose_name = 'Nome', max_length = 50, default="Nome")
	rg = models.DecimalField(verbose_name = 'rg', max_digits = 10, decimal_places = 0, default=0 ) 

	def __unicode__(self):
		return self.nome
		