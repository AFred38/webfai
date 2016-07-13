from django.contrib import admin

# Register your models here.

from .models import Machine
admin.site.register(Machine)

from .models import Archi
admin.site.register(Archi)

from .models import Distrib
admin.site.register(Distrib)
from .models import Action
admin.site.register(Action)
from .models import Profil
admin.site.register(Profil)
from .models import Clavier
admin.site.register(Clavier)
from .models import Equipe
admin.site.register(Equipe)
from .models import Wm 
admin.site.register(Wm)
from .models import Auth 
admin.site.register(Auth)
