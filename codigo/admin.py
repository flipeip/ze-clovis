"""
Registro dos modelos no sistema de administrador do Django
"""

from django.contrib import admin
from .models import Config, Admin, UsuarioCadastrado, Ficha

admin.site.register(Config)
admin.site.register(Admin)
admin.site.register(UsuarioCadastrado)
admin.site.register(Ficha)
