from django.contrib import admin
from .models import Cliente, Endereco

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ("criado_em","atualizado_em")
    
    class Media:
        js = ("clientes/js/cliente_admin.js",)

admin.site.register(Endereco)