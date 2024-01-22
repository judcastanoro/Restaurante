from django.contrib import admin
from .models.user import User
from .models.cliente import Cliente
from .models.plato import Plato
from .models.mesa import Mesa
from .models.reserva import Reserva

# Register your models here.
admin.site.register(User)
admin.site.register(Cliente)
admin.site.register(Plato)
admin.site.register(Mesa)
admin.site.register(Reserva)