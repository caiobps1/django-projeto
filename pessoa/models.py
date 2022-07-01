from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)
    #metodo pra exibir nome certo
    def __str__(self):
        return self.nome_completo
