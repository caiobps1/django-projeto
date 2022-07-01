from django.urls import path
from .views import PrincipalView # chama a classe

urlpatterns = [
    path('', PrincipalView.as_view(), name='principal')
]
