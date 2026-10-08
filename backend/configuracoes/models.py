from django.db import models

# Create your models here.
class configuracao(models.Model):
    chave = models.CharField(
        max_length=100,
        unique=True
    )
    valor = models.TextField()
    atualizado_em = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return self.chave