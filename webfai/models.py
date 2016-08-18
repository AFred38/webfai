# coding: utf8
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

ARCHIS = (('x32','I386'),('x64','AMD64'))
DISTRIS = (('Stable','JESSIE'),('Testing','STRETCH'))
ACTIONS = (('Installation','INSTALL'),('Mise a jour','MAJ'))
PROFILS = (('Station','LJK_STATION'),('Serveur de Calcul','LJK_SERV_CALCUL'),('Serveur','LJK_SERV'))
EQUIPES = (('Airsea','EQUIPE_AIRSEA'),('Casys','EQUIPE_CASYS'),('Cvgi','EQUIPE_CVGI'),('Dea','EQUIPE_DEA'),('Edp','EQUIPE_EDP'),('Ips','EQUIPE_IPS'),('Sagag','EQUIPE_SAGAG'),('Sam','EQUIPE_SAM'),('Staff','EQUIPE_STAFF'))
WMS = (('Tous','TOUS'),('Gnome','GNOME'),('Kde','KDE'),('IceWM','ICEWM'),('Enlightenment','E17'))
CLAVIERS = (('Fr','AZERTY'),('Us','QWERTY'),('Uk','QWERTY_UK'))
AUTHS = (('Local','LOCAL'),('Ldap','LDAP'))



@python_2_unicode_compatible
class Auth(models.Model):
        name = models.CharField(max_length=10,verbose_name="Authentification",choices=AUTHS)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name

class Clavier(models.Model):
        name = models.CharField(max_length=20,verbose_name="Clavier",choices=CLAVIERS)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name

class Wm(models.Model):
        name = models.CharField(max_length=20,verbose_name="Window Manager",choices=WMS)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name

class Equipe(models.Model):
        name = models.CharField(max_length=30,verbose_name="Equipe",choices=EQUIPES)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name

class Profil(models.Model):
        name = models.CharField(max_length=30,verbose_name="Profil",choices=PROFILS)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name

class Action(models.Model):
        name = models.CharField(max_length=20,verbose_name="FAI Action",choices=ACTIONS)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name


class Archi(models.Model):
        name = models.CharField(max_length=20,verbose_name="Architecture",choices=ARCHIS)
        #DEFAULT_PK=1
	def __str__(self):
                return self.name

class Distrib(models.Model):
        name = models.CharField(max_length=20,verbose_name="Distribution",choices=DISTRIS)
        #DEFAULT_PK=1
        def __str__(self):
                return self.name

class Machine(models.Model):
        name = models.CharField(max_length=30, blank=False, verbose_name="Nom")
        addr = models.CharField(max_length=17, blank=False, verbose_name="Adresse MAC")
        archi = models.ForeignKey(Archi, default=1, verbose_name="Architecture")
        distri = models.ForeignKey(Distrib, default=1, verbose_name="Distribution")
        action = models.ForeignKey(Action, default=1, verbose_name="FAI Action")
        profil = models.ForeignKey(Profil, default=1, verbose_name="Profil")
        clavier = models.ForeignKey(Clavier, default=1, verbose_name="Clavier")
	equipe = models.ForeignKey(Equipe, default=1, verbose_name="Equipe")
        wm = models.ForeignKey(Wm, default=1, verbose_name="Window Manager")
        auth = models.ForeignKey(Auth, default=1, verbose_name="Authentification")
        gl_drivers = models.BooleanField(default=False, verbose_name="Drivers Nvidia OpenGL")
        def __str__(self):
                return self.name
	def get_absolute_url(self):
		return reverse('details',kwargs={'pk':self.pk})

class MachineForm(ModelForm):
        class Meta:
                model = Machine
                #fields = ['name', 'addr', 'archi', 'distri', 'action', 'profil', 'equipe', 'clavier', 'wm', 'gl_drivers', 'auth' ]
                fields = '__all__'

