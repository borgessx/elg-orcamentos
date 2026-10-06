from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(
        max_length = 150,
        unique=True
    )
    descricao = models.TextField(
        blank=True
    )
    ativo = models.BooleanField(
        default=True
    )
    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.PROTECT,
        related_name = "produtos"
    )
    codigo = models.CharField(
        max_length = 50,
        unique=True
    )
    nome = models.CharField(
        max_length = 150
    )
    descricao = models.TextField(
        blank = True
    )
    altura_mm = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    largura_mm = models.DecimalField(
        max_digits = 10,
        decimal_places =2
    )
    profundidade_mm = models.DecimalField(
        max_digits =10,
        decimal_places=2
    )
    material = models.CharField(
        max_length = 150
    )
    espressura_mm = models.DecimalField(
        max_digits=10,
        decimal_places =2
    )
    acabamento = models.CharField(
        max_length = 150
    )
    preco_base = models.DecimalField(
        max_digits = 20,
        decimal_places = 2
    )
    ativo = models.BooleanField(
        default=True
    )
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    atualizado_em = models.DateTimeField(
        auto_now = True
    )
    def __str__(self):
        return self.nome
