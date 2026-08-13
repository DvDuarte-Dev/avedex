from src.avedex.utils import (
    valor_ou_indisponivel,
    cortar_texto,
    titulo,
    linha,
)
from src.avedex.catalogo import escolher_ave


LARGURA_COLUNA = 25
TAMANHO_SEPARADOR = 75


CAMPOS_COMPARACAO = [
    ("Nome científico", "nome_cientifico", ""),
    ("Família", "familia", ""),
    ("Ordem", "ordem", ""),
    ("Dieta", "dieta_tipo", ""),
    ("Habitat", "habitat", ""),
    ("Comprimento (cm)", "comprimento_cm", "cm"),
    ("Peso (g)", "peso_g", "g"),
    ("Status", "status_conservacao", ""),
]


def preparar_valor_comparacao(ave, campo, unidade):
    valor = ave.get(campo)

    if campo == "habitat":
        return cortar_texto(valor, 25)

    return valor_ou_indisponivel(
        valor,
        unidade
    )


def imprimir_linha_comparacao(
    rotulo,
    valor1,
    valor2
):
    valor1 = valor_ou_indisponivel(valor1)
    valor2 = valor_ou_indisponivel(valor2)

    print(
        f"{rotulo:<{LARGURA_COLUNA}}"
        f"{str(valor1):<{LARGURA_COLUNA}}"
        f"{str(valor2):<{LARGURA_COLUNA}}"
    )


def comparar_aves(ave1, ave2):
    titulo("COMPARAÇÃO DE AVES")

    print(
        f"{'Característica':<{LARGURA_COLUNA}}"
        f"{ave1['nome_popular']:<{LARGURA_COLUNA}}"
        f"{ave2['nome_popular']:<{LARGURA_COLUNA}}"
    )

    print(linha("-", TAMANHO_SEPARADOR))

    for rotulo, campo, unidade in CAMPOS_COMPARACAO:
        valor1 = preparar_valor_comparacao(
            ave1,
            campo,
            unidade
        )

        valor2 = preparar_valor_comparacao(
            ave2,
            campo,
            unidade
        )

        imprimir_linha_comparacao(
            rotulo,
            valor1,
            valor2
        )

    print()
    print(linha("-", TAMANHO_SEPARADOR))

    if ave1["peso_g"] > ave2["peso_g"]:
        print(
            f"{ave1['nome_popular']} é mais pesada que "
            f"{ave2['nome_popular']}."
        )

    elif ave2["peso_g"] > ave1["peso_g"]:
        print(
            f"{ave2['nome_popular']} é mais pesada que "
            f"{ave1['nome_popular']}."
        )

    else:
        print(
            "As duas aves possuem o mesmo peso."
        )


def tela_comparacao(catalogo):
    titulo("COMPARAÇÃO DE AVES")

    ave1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    if ave1 is None:
        return

    ave2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    if ave2 is None:
        return

    if ave1["id"] == ave2["id"]:
        print(
            "Escolha duas aves diferentes."
        )
        return

    comparar_aves(
        ave1,
        ave2
    )