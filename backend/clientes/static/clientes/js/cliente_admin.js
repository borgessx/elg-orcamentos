document.addEventListener("DOMContentLoaded", function () {
    const tipoPessoa = document.getElementById("id_tipo_pessoa");
    const rotuloNome = document.querySelector(
        'label[for="id_nome_razao_social"]'
    );

    if (!tipoPessoa || !rotuloNome) {
        return;
    }

    function atualizarRotulo() {
        if (tipoPessoa.value === "PF") {
            rotuloNome.textContent = "Nome completo:";
        } else if (tipoPessoa.value === "PJ") {
            rotuloNome.textContent = "Razão social:";
        } else {
            rotuloNome.textContent = "Nome / Razão social:";
        }
    }

    tipoPessoa.addEventListener("change", atualizarRotulo);
    atualizarRotulo();
});
