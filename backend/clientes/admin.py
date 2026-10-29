from django.contrib import admin
from .models import Cliente, Endereco

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nome_razao_social",
        "tipo_pessoa",
        "cpf_cnpj",
        "email",
        "ativo",
    )
    search_fields = (
        "nome_razao_social",
        "nome_fantasia",
        "cpf_cnpj",
        "email",
    )
    list_filter = ("tipo_pessoa","ativo")
    ordering = ("nome_razao_social",)

    readonly_fields = ("criado_em","atualizado_em")

    class Media:
        js = ("clientes/js/cliente_admin.js",)

admin.site.register(Endereco)