from django.db import models

from .imoveis import Imoveis

class Comodidade(models.Model):
    estacionamento = models.CharField(max_length=255, blank=True, null=True)
    acessibilidade = models.CharField(max_length=255, blank=True, null=True)
    seguranca = models.CharField(max_length=255, blank=True, null=True)
    tecnologia = models.CharField(max_length=255, blank=True, null=True)
    imoveis = models.ForeignKey(Imoveis, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.tecnologia