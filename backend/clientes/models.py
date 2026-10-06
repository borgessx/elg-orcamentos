from django.db import models

class Cliente(models.Model):
    class TipoPessoa(models.TextChoices):
        FISICA = "PF","Pessoa Física"
        JURIDICA = "PJ","Pessoa Jurídica"
    tipo_pessoa = models.CharField(
        max_length=2,
        choices=TipoPessoa.choices
    )
    nome_razao_social = models.CharField(
        max_length=20
    )
    nome_fantasia = models.CharField(
        max_length=150,
        blank=True
    )
    cpf_cnpj = models.CharField(
        max_length=14,
        unique=True
    )
    email = models.EmailField(
        unique=True
    )
    telefone = models.CharField(
        max_length=20,
        unique=True
    )
    ativo = models.BooleanField(
        default=True
    )
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    atualizado_em = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.nome_razao_social

class Endereco(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="enderecos"
    )
    cep = models.CharField(
        max_length=8
    )
    longadouro =  models.CharField(
        max_length=150
    )
    numero = models.CharField(
        max_length=20
    )
    complemento = models.CharField(
        max_length=100,
        blank=True
    )
    bairro = models.CharField(
        max_length=100
    )
    cidade = models.CharField(
        max_length=100
    )
    uf = models.CharField(
        max_length=2
    )
    principal = models.BooleanField(
        default=False
    )
    def __str__(self):
        return f"{self.longadouro}, {self.numero} - {self.cidade}/{self.uf}"
    

