from django.db import models
from django.conf import settings
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

class SolicitacaoPersonalizada(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="solicitacoe_personalizadas"
    )
    usuario_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="solicitacoes_responsavel"
    )
    protocolo = models.CharField(
        max_length=50,
        unique=True
    )
    descricao = models.TextField()
    quantidade = models.IntegerField()
    status = models.CharField(
        max_length=30
    )
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    atualizado_em = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return f"{self.protocolo} - {self.cliente.nome_razao_social}"
    
class Orcamento(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete = models.PROTECT,
        related_name = "orcamento"
    )
    usuario_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.PROTECT,
        related_name="orcamentos_responsavel"
    )
    protocolo = models.CharField(
        max_length=50,
        unique=True
    )
    status = models.CharField(
        max_length = 30
    )
    cliente_nome_snapshot = models.CharField(
        max_length = 150 
    )
    cliente_documento_snapshot = models.CharField(
        max_length = 14
    )
    cliente_email_snapshot = models.EmailField()
    cliente_telefone_snapshot = models.CharField(
        max_length = 20
    )
    endereco_snapshot = models.TextField()
    valor_total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    observacoes=models.TextField()
    validade = models.DateField()
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    atualizado_em=models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return f"{self.protocolo} - {self.cliente_nome_snapshot}"

class OrcamentoItem(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete = models.CASCADE,
        related_name = "itens"
    )
    produto = models.ForeignKey(
        Produto,
        on_delete = models.PROTECT,
        related_name="itens_orcamento"
    )
    produto_codigo_snapshot = models.CharField(
        max_length=50
    )
    produto_nome_snapshot = models.CharField(
        max_length = 150
    )
    especificacoes_snapshot = models.TextField()
    quantidade = models.IntegerField()
    preco_unitario=models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    subtotal=models.DecimalField(
        max_digits=12,
        decimal_places=2,
        editable=False
    )
    def save(self,*args, **kwargs):
        self.subtotal = self.preco_unitario * self.quantidade
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.produto_nome_snapshot} - Quantidade: {self.quantidade}"

    