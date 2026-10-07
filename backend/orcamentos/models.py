from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

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

class ListaOrcamentoItem(models.Model):
    lista = models.ForeignKey(
        ListaOrcamento,
        on_delete=models.CASCADE,
        related_name="itens"
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name="itens"
    )
    quantidade = models.IntegerField()
    def __str__(self):
        return f"{self.produto.nome} - Quantidade:{self.quantidade}"

