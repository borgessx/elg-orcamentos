from django.db import models
from django.conf import settings
# Create your models here.

class LogAuditoria(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="logs_auditoria"
    )
    acao = models.CharField(
        max_length=50
    )
    entidade = models.CharField(
        max_length=100
    )
    registro_id = models.CharField(
        max_length=100
    )
    dados_alterado = models.JSONField()
    criado_em = models.DateTimeField(
        auto_now=True
    )
    def __str__(self) -> str:
        return f"{self.usuario} - {self.acao} - {self.entidade}"
    
