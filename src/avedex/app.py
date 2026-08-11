from src.avedex.dados import carregar_aves

from src.avedex.interface import (
    exibir_linha,
    exibir_menu,
    mostrar_boas_vindas,
    mostrar_sobre,
    pausar,
)

from src.avedex.catalogo import (
    listar_aves,
    tela_busca,
    selecionar_ave_por_id,
)

from src.avedex.comparacao import tela_comparacao

def processar_opcao(opcao, catalogo):
    if opcao == "1":
        listar_aves(catalogo)

    elif opcao == "2":
        tela_busca(catalogo)

    elif opcao == "3":
        selecionar_ave_por_id(catalogo)

    elif opcao == "4":
        tela_comparacao(catalogo)

    elif opcao == "5":
        mostrar_sobre()

    elif opcao == "0":
        print("Encerrando a AveDex.")

    else:
        print(
            "Opção inválida. "
            "Digite apenas 0, 1, 2, 3, 4 ou 5."
        )

def executar():
    catalogo_aves = carregar_aves()
    
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