from django.contrib import admin

from .models import Contato

# Register your models here.

#@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'sexo', 'cidade')
	search_fields = ('nome', 'email')

admin.site.register(Contato, ContatoAdmin)