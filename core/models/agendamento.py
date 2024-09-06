from django.db import models

from .imoveis import Imoveis

class Agendamento(models.Model):
    contato_corretor = models.CharField(max_length=11, unique=True, blank=True, null=True)
    disponibilidade = models.BooleanField(default=True)
    definicao_data = models.DateTimeField()
    confirmacao = models.BooleanField(default=False)
    imoveis = models.ForeignKey(Imoveis, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.contato_corretor