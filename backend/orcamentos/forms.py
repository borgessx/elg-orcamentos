from django import forms

from clientes.models import Endereco
from .models import Orcamento


class EnderecoChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, endereco):
        return f"{endereco.cliente} — {endereco}"


class OrcamentoAdminForm(forms.ModelForm):
    endereco_selecionado = EnderecoChoiceField(
        queryset=Endereco.objects.select_related("cliente"),
        label="Endereço do orçamento",
        help_text="Escolha um endereço pertencente ao cliente selecionado.",
        required=True,
    )

    class Meta:
        model = Orcamento
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance._state.adding:
            self.fields.pop("endereco_selecionado", None)

    def clean(self):
        dados = super().clean()

        if self.instance._state.adding:
            cliente = dados.get("cliente")
            endereco = dados.get("endereco_selecionado")

            if cliente and endereco:
                if endereco.cliente_id != cliente.pk:
                    self.add_error(
                        "endereco_selecionado",
                        "Este endereço não pertence ao cliente selecionado.",
                    )

        return dados

    def save(self, commit=True):
        orcamento = super().save(commit=False)

        if orcamento._state.adding:
            endereco = self.cleaned_data["endereco_selecionado"]

            partes = [
                f"{endereco.longadouro}, {endereco.numero}",
            ]

            if endereco.complemento:
                partes.append(endereco.complemento)

            partes.extend([
                endereco.bairro,
                f"{endereco.cidade}/{endereco.uf}",
                f"CEP: {endereco.cep}",
            ])

            orcamento.endereco_snapshot = " - ".join(partes)

        if commit:
            orcamento.save()
            self.save_m2m()

        return orcamento