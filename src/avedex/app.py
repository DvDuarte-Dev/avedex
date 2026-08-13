from src.avedex.ambiente import verificar_ambiente
from src.avedex.creditos import mostrar_creditos

from src.avedex.dados import (
    carregar_aves,
    validar_dataset,
)

from src.avedex.interface import (
    exibir_linha,
    exibir_menu,
    mostrar_boas_vindas,
    mostrar_sobre,
    pausar,
)

from src.avedex.catalogo import (
    listar_aves,
    buscar_ave_por_id,
    buscar_aves,
    exibir_resultados_busca,
    selecionar_resultado_busca,
    tela_busca,
    exibir_detalhes_ave,
    selecionar_ave_por_id,
    escolher_ave,
    mostrar_ave_aleatoria,
)

from src.avedex.comparacao import tela_comparacao

from src.avedex.batalha import batalha_avedex

def processar_opcao(opcao, catalogo):
    if opcao == "1":
        listar_aves(catalogo)

    elif opcao == "2":
        tela_busca(catalogo)

    elif opcao == "3":
        mostrar_ave_aleatoria(catalogo)

    elif opcao == "4":
        selecionar_ave_por_id(catalogo)

    elif opcao == "5":
        tela_comparacao(catalogo)

    elif opcao == "6":
        batalha_avedex(
            catalogo,
            escolher_ave
        )

    elif opcao == "7":
        verificar_ambiente()

    elif opcao == "8":
        mostrar_creditos()

    elif opcao == "0":
        print("Encerrando a AveDex.")

    else:
        print(
            "Opção inválida. "
            "Digite 0, 1, 2, 3, 4, 5, 6, 7 ou 8."
        )

def executar():
    catalogo_aves = carregar_aves()

    problemas = validar_dataset(catalogo_aves)

    if problemas:
        print("[AVISO] O dataset possui problemas:")

        for problema in problemas:
            print(f"- {problema}")
    
    exibir_linha()
    print("AVEDEX")
    exibir_linha()

    nome_usuario = input(
        "Digite seu nome: "
    ).strip()

    mostrar_boas_vindas(nome_usuario)

    opcao_menu = ""

    while opcao_menu != "0":
        exibir_menu()

        opcao_menu = input(
            "Escolha uma opção: "
        ).strip()

        print()

        processar_opcao(
            opcao_menu,
            catalogo_aves
        )

        if opcao_menu == "0":
            print(f"Até logo, {nome_usuario}!")

        if opcao_menu != "0":
            pausar()