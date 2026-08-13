import random

from src.avedex.interface import exibir_titulo
from src.avedex.utils import (
    normalizar_texto,
    mensagem_aviso,
    pausar,
)

def listar_aves(catalogo):
    return paginar_aves(
        catalogo,
        "AVES CADASTRADAS"
    )

def mostrar_ave_aleatoria(catalogo):
    if not catalogo:
        mensagem_aviso(
            "Nenhuma ave disponível para sorteio."
        )
        return

    ave = random.choice(catalogo)

    exibir_titulo("AVE ALEATÓRIA")

    print(
        f"Ave sorteada: "
        f"{ave.get('nome_popular', 'Ave')}"
    )

    exibir_detalhes_ave(ave)

def ler_comando_paginacao():
    print()
    print("ENTER - próxima página")
    print("p - página anterior")
    print("q - sair")
    print("ID - escolher uma ave")

    return input("Comando: ").strip().lower()


def paginar_aves(aves, titulo_lista="AVES", tamanho_pagina=10):
    if not aves:
        mensagem_aviso("Nenhuma ave disponível.")
        return None

    pagina = 0

    while True:
        total = len(aves)

        inicio = pagina * tamanho_pagina
        fim = inicio + tamanho_pagina

        aves_pagina = aves[inicio:fim]

        total_paginas = (
            total + tamanho_pagina - 1
        ) // tamanho_pagina

        exibir_titulo(
            f"{titulo_lista} - página "
            f"{pagina + 1} de {total_paginas}"
        )

        for ave in aves_pagina:
            identificador = ave.get("id", "-")
            nome = ave.get(
                "nome_popular",
                "Nome não informado"
            )
            familia = ave.get("familia", "-")

            print(
                f"{str(identificador):>3} - "
                f"{nome} ({familia})"
            )

        print()

        print(
            f"Mostrando {inicio + 1} a "
            f"{min(fim, total)} de {total} aves."
        )

        comando = ler_comando_paginacao()

        if comando == "":
            if fim < total:
                pagina += 1
            else:
                mensagem_aviso(
                    "Você já está na última página."
                )
                pausar()

        elif comando == "p":
            if pagina > 0:
                pagina -= 1
            else:
                mensagem_aviso(
                    "Você já está na primeira página."
                )
                pausar()

        elif comando == "q":
            return None

        elif comando.isdigit():
            for ave in aves:
                if str(ave.get("id")) == comando:
                    return ave

            mensagem_aviso("ID não encontrado.")
            pausar()

        else:
            mensagem_aviso("Comando inválido.")
            pausar()

def ler_id_ave(mensagem):
    while True:
        entrada = input(mensagem).strip()

        if entrada.isdigit():
            return int(entrada)

        mensagem_aviso("Digite apenas números.")

def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if ave["id"] == id_procurado:
            return ave

    return None

def buscar_aves(catalogo, termo_busca):
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        texto_busca = " ".join(campos_busca)
        texto_busca = normalizar_texto(texto_busca)

        if termo in texto_busca:
            resultados.append(ave)

    return resultados

def exibir_resultados_busca(resultados):
    exibir_titulo("RESULTADOS DA BUSCA")

    print(f"Foram encontradas {len(resultados)} ave(s).\n")

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )

def selecionar_resultado_busca(resultados):
    escolha = input(
        "\nDigite o ID para ver detalhes ou ENTER para voltar: "
    ).strip()

    if escolha == "":
        return

    ave_encontrada = buscar_ave_por_id(
        resultados,
        escolha
    )

    if ave_encontrada is None:
        print("ID não encontrado nos resultados.")
    else:
        exibir_detalhes_ave(ave_encontrada)

def tela_busca(catalogo):
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    resultados = buscar_aves(catalogo, termo)

    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        selecionar_resultado_busca(resultados)

def exibir_detalhes_ave(ave):
    exibir_titulo("DETALHES DA AVE")

    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(
        f"Curiosidade: "
        f"{ave.get('curiosidade', 'Não informada')}"
    )

def selecionar_ave_por_id(catalogo):
    ave_encontrada = listar_aves(catalogo)

    if ave_encontrada is not None:
        exibir_detalhes_ave(ave_encontrada)

def escolher_ave(catalogo, mensagem):
    listar_aves(catalogo)

    id_escolhido = ler_id_ave(
        f"\n{mensagem}: "
    )

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso(
            "Ave não encontrada. Confira o ID informado."
        )
        return None

    return ave_encontrada