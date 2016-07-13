# coding: utf8
from django.shortcuts import get_object_or_404,render
from django.views import generic
from django.core.urlresolvers import reverse

# Create your views here.

from .models import Machine, MachineForm
from wakeonlan import wol

def index(request):
	"""Liste le parc"""
	Liste_parc = Machine.objects.all()
	context = {'Liste_parc':Liste_parc}
        return render(request, 'webfai/index.html', context )

class IndexView(generic.ListView):
	template_name = 'webfai/index.html'
	context_object_name = 'Liste_parc'

	def get_queryset(self):
		"""retourne la liste du parc"""
		return Machine.objects.all()

def wakeup(request,machine_pk):
	"""Reveille une machine en WakeOnLan"""
	machine = get_object_or_404(Machine, pk=machine_pk) 
	wol.send_magic_packet(machine.addr)
	context = {'machine_name': machine.name}
	return render(request, 'webfai/wakeup.html', context) 

def modify(request,machine_pk):
	"""Modifier une machine"""
	machine = get_object_or_404(Machine, pk=machine_pk)
	#context = {'machine': machine}
	context = {'machine':MachineForm(instance=machine)}
	return render(request, 'webfai/modify.html', context)

def clone(request,machine_pk):
	"""Cloner une machine"""
	machine = get_object_or_404(Machine,pk=machine_pk)
	context = {'machine_name': machine.name}
	return render(request,'webfai/clone.html',context)

def delete(request,machine_pk):
	"""Supprimer une machine"""
	machine = get_object_or_404(Machine,pk=machine_pk)
	context = {'machine_name': machine.name}
	return render(request, 'webfai/delete.html', context)

