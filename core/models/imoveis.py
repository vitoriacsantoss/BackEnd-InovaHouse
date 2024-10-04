from django.db import models
from uploader.models import Image

from .categoria import Categoria

class Imoveis(models.Model):
    codigo = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)  
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    localizacao = models.CharField(max_length=255, blank=True, null=True)
    metragem = models.IntegerField(blank=True, null=True)
    quantidade_quarto = models.IntegerField(default=1)
    quantidade_banheiro = models.IntegerField(default=1)
    quantidade_suite = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    categorias = models.ManyToManyField(Categoria, blank=True) 

    def __str__(self):
        return f'{self.codigo} - {self.localizacao}'

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
