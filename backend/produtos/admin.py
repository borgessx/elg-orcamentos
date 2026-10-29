from django.contrib import admin
from .models import Categoria, Produto, ProdutoImagem

class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 1
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (ProdutoImagemInline,)

    list_display = (
        "codigo",
        "nome",
        "categoria",
        "preco_base",
        "ativo",
    )
    search_fields = ("codigo", "nome")
    list_filter = ("categoria", "ativo")
    ordering = ("nome",)
    list_select_related = ("categoria",)
admin.site.register(Categoria)
admin.site.register(ProdutoImagem)