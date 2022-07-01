from msilib.schema import ListView
from django.shortcuts import render

from django.views.generic import ListView
from .models import Pessoa

# Create your views here.

class ListaPessoaView(ListView):
    model = Pessoa
    queryset: Pessoa.objects.all().order_by('nome_completo')