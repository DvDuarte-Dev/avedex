from src.avedex.utils import (
    valor_ou_indisponivel,
    mensagem_aviso,
    titulo,
)


ATRIBUTOS_BATALHA = [
    ("1", "Comprimento", "comprimento_cm", "cm"),
    ("2", "Peso médio", "peso_g", "g"),
    ("3", "Índice de conservação", "indice_conservacao", ""),
]


def mostrar_atributos_batalha(ave):
    print(
        f"\n{ave.get('nome_popular', 'Ave')}"
    )

    for numero, nome, campo, unidade in ATRIBUTOS_BATALHA:
        valor = ave.get(campo)

        print(
            f"{numero} - {nome}: "
            f"{valor_ou_indisponivel(valor, unidade)}"
        )


def escolher_atributo():
    print("\nEscolha o atributo da batalha:")

    for numero, nome, _, _ in ATRIBUTOS_BATALHA:
        print(f"{numero} - {nome}")

    escolha = input("Atributo: ").strip()

    for numero, nome, campo, unidade in ATRIBUTOS_BATALHA:
        if escolha == numero:
            return nome, campo, unidade

    mensagem_aviso("Atributo inválido.")
    return None


def batalha_avedex(aves, escolher_ave):
    titulo("BATALHA AVEDEX")

    ave_1 = escolher_ave(
        aves,
        "Escolha a primeira ave da batalha"
    )

    if ave_1 is None:
        return

    ave_2 = escolher_ave(
        aves,
        "Escolha a segunda ave da batalha"
    )

    if ave_2 is None:
        return

    if ave_1["id"] == ave_2["id"]:
        mensagem_aviso(
            "Escolha duas aves diferentes."
        )
        return

    atributo = escolher_atributo()

    if atributo is None:
        return

    nome, campo, unidade = atributo

    valor_1 = ave_1.get(campo)
    valor_2 = ave_2.get(campo)

    if not isinstance(valor_1, (int, float)):
        mensagem_aviso(
            f"{ave_1['nome_popular']} não possui "
            f"valor válido para {nome.lower()}."
        )
        return

    if not isinstance(valor_2, (int, float)):
        mensagem_aviso(
            f"{ave_2['nome_popular']} não possui "
            f"valor válido para {nome.lower()}."
        )
        return

    print()
    print(
        f"{nome}: "
        f"{valor_ou_indisponivel(valor_1, unidade)} "
        f"vs "
        f"{valor_ou_indisponivel(valor_2, unidade)}"
    )

    if valor_1 > valor_2:
        print(
            f"🏆 {ave_1['nome_popular']} venceu!"
        )

    elif valor_2 > valor_1:
        print(
            f"🏆 {ave_2['nome_popular']} venceu!"
        )

    else:
        print("⚔️ Empate!")