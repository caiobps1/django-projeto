from django.shortcuts import render

# Ajuda pra renderizar as views
from django.views.generic import TemplateView

# Create your views here.

class PrincipalView(TemplateView):
    template_name = 'principal/index.html'