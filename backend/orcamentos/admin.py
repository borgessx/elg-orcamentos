from django.contrib import admin
from .models import ListaOrcamento, ListaOrcamentoItem,SolicitacaoPersonalizada,Orcamento,OrcamentoItem

class OrcamentosItemInline(admin.StackedInline):
    model = OrcamentoItem
    extra = 1
    readonly_fields = ("subtotal",)

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    inlines = (OrcamentosItemInline,)

    readonly_fields = (
        "valor_total",
        "cliente_nome_snapshot",
        "cliente_documento_snapshot",
        "cliente_email_snapshot",
        "cliente_telefone_snapshot",
    )

    def get_readonly_fields(self, request, obj=None):
        campos = super().get_readonly_fields(request, obj)

        if obj is not None:
            return campos + ("cliente",)

        return campos
    

admin.site.register(ListaOrcamento)
admin.site.register(ListaOrcamentoItem)
admin.site.register(SolicitacaoPersonalizada)

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
