from django.contrib import admin
from .models import ListaOrcamento, ListaOrcamentoItem,SolicitacaoPersonalizada,Orcamento,OrcamentoItem
# Register your models here.
admin.site.register(ListaOrcamento)
admin.site.register(ListaOrcamentoItem)
admin.site.register(SolicitacaoPersonalizada)
admin.site.register(Orcamento)
class OrcamentoItemAdmin(admin.ModelAdmin):
    readonly_field=("subtotal",)
    list_display=(
        "orcamento",
        "produto",
        "quantidade",
        "preco_unitario",
        "subtotal",
    )
admin.site.register(OrcamentoItem,OrcamentoItemAdmin)
