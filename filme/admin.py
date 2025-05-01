from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
campo = list(UserAdmin.fieldsets)
campo.append(
    ("Filmes Vistos", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campo)

admin.site.register(Filme)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Pergunta)
admin.site.register(Episodio)
admin.site.register(Buscadecategorias)