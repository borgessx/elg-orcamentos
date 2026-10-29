from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .models import Orcamento, OrcamentoItem


@receiver(pre_save, sender=OrcamentoItem)
def lembrar_orcamento_anterior(sender, instance, raw=False, **kwargs):
    if raw:
        return

    instance._orcamento_anterior_id = None

    if instance.pk:
        instance._orcamento_anterior_id = (
            OrcamentoItem.objects
            .filter(pk=instance.pk)
            .values_list("orcamento_id", flat=True)
            .first()
        )


@receiver(post_save, sender=OrcamentoItem)
def atualizar_total_apos_salvar(sender, instance, raw=False, **kwargs):
    if raw:
        return

    orcamentos_ids = {
        instance.orcamento_id,
        getattr(instance, "_orcamento_anterior_id", None),
    }

    for orcamento in Orcamento.objects.filter(pk__in=orcamentos_ids):
        orcamento.recalcular_total()


@receiver(post_delete, sender=OrcamentoItem)
def atualizar_total_apos_excluir(sender, instance, **kwargs):
    orcamento = (
        Orcamento.objects
        .filter(pk=instance.orcamento_id)
        .first()
    )

    if orcamento is not None:
        orcamento.recalcular_total()