from django.contrib import admin
from .models import Categoria, Produto, ProdutoImagem

class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 1
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (ProdutoImagemInline,)

admin.site.register(Categoria)
admin.site.register(ProdutoImagem)