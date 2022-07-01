from django.contrib import admin
from .models import Pessoa, Contato

# Register your models here.


class pessoaAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'data_nascimento', 'ativa']
    list_filter = [
        'ativa',
        'data_nascimento'
    ]
    search_fields = [
        'nome_completo'
    ]


admin.site.register(Pessoa, pessoaAdmin)
admin.site.register(Contato)