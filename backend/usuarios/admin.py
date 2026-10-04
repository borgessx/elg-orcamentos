from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Dados da ELG", {"fields": ("perfil",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Dados da ELG", {"fields": ("perfil",)}),
    )