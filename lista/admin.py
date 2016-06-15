# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
class ParticipanteAdmin(admin.ModelAdmin):	
	search_fields = ['nome','rg']
	list_display = ['nome','rg']
	fieldsets = ((None,{'fields': ('nome','rg')}), )
	list_filter = ['nome','rg']
	save_on_top = True

admin.site.register(Participante,ParticipanteAdmin)