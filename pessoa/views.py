from msilib.schema import ListView
from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse, Http404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa, Contato
from .forms import PessoaForm, ContatoForm
from django.urls import reverse

# Create your views here.

class ListaContatoView(ListView):
    model = Contato
    queryset: Contato.objects.all().order_by('nome')

class ListaPessoaView(ListView):
    model = Pessoa
    queryset: Pessoa.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
            
        return queryset

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    sucess_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'

# CONTATOS


def contatos(request, pk_pessoa):
    contatos = Contato.objects.filter(pessoa=pk_pessoa)
    return render(request, 'contato/contato_list.html', {'contatos': contatos, 'pk_pessoa': pk_pessoa})


def contato_novo(request, pk_pessoa):
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.pessoa_id = pk_pessoa;
            contato.save()
            return redirect(reverse('pessoa.contatos', args=[pk_pessoa]))

    return render(request, 'contato/contato_form.html', {'form': form})


def contato_editar(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(instance=contato)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa.contatos', args=[pk_pessoa]))

    return render(request, 'contato/contato_form.html', {'form': form})


def contato_remover(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk)
    contato.delete()
    return redirect(reverse('pessoa.contatos', args=[pk_pessoa]))