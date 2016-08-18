# coding: utf8
from django.shortcuts import get_object_or_404,render
from django.views import generic
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

INDEX_URL = reverse_lazy('index')
DETAILS_URL = reverse_lazy('details')

# Create your views here.

from .models import Machine, MachineForm
from wakeonlan import wol

#def index(request):
#	"""Liste le parc"""
#	Liste_parc = Machine.objects.all()
#	context = {'Liste_parc':Liste_parc}
#        return render(request, 'webfai/index.html', context )

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
	context = {'machine':MachineForm(instance=machine),'pk':machine_pk}
	return render(request, 'webfai/modify.html', context)

class modified(UpdateView):
	"""Modifie une machine"""
	model = Machine
	fields = ['action','archi','distri','profil','clavier','equipe','wm','gl_drivers','auth']
	#success_url = DETAILS_URL
	#pk_url_kwarg = 'machine_pk'

def clone(request,machine_pk):
	"""Cloner une machine"""
	machine = get_object_or_404(Machine,pk=machine_pk)
	context = {'machine_name': machine.name}
	return render(request,'webfai/clone.html',context)

def delete(request,machine_pk):
	"""Supprimer une machine"""
	machine = get_object_or_404(Machine,pk=machine_pk)
	context = {'machine': machine}
	return render(request, 'webfai/delete.html', context)

class deleted(generic.DeleteView):
	"""suppression d'une machine"""
	model = Machine
	success_url = INDEX_URL

#def details(request,machine_pk):
#	MachineInfos = get_object_or_404(Machine,pk=machine_pk)
#	context = {'MachineInfos':MachineInfos}
#	return render(request, 'webfai/details.html', context )

class details(generic.DetailView):
	model = Machine
	template_name = 'webfai/details.html'
	#pk_url_kwarg = 'machine_pk'
	

