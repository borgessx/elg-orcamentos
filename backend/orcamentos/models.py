from django.db import models
from clientes.models import Cliente

# Create your models here.
class ListaOrcamento(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name = "listas_orcamento"
    )
    criado_em = models.DateTimeField(
        auto_now_add = True
    )
    atualizado_em = models.DateTimeField(
        auto_now = True
    )
    def __str__(self):
        return f"Lista {self.id} - {self.cliente.nome_razao_social}"

class

