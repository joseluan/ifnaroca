# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from lista.models import *

def lista(request):
	cadastro = False
	Nparticipantes = len(Participante.objects.all())
	if request.method=='POST':
		try:
			Participante.objects.get(rg=request.POST.get("RG"))
		except Exception, e:
			cadastro = True
			Participante.objects.create(nome=request.POST.get("nome"),rg=request.POST.get("RG")).save()
			Nparticipantes = len(Participante.objects.all())
			return render(request,'lista.html',{'cadastro': True,'Nparticipantes':Nparticipantes})
		return render(request,'lista.html',{'cadastro': True,'Nparticipantes':Nparticipantes})


	else:
		return render(request,'lista.html',{'cadastro': cadastro,'Nparticipantes':Nparticipantes})

def index(request):
	return render(request,'index.html',{})