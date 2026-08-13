from src.avedex.ambiente import verificar_ambiente
from src.avedex.creditos import mostrar_creditos

from src.avedex.dados import (
    carregar_aves,
    validar_dataset,
)

from src.avedex.interface import (
    abertura,
    exibir_menu_principal,
)

from src.avedex.utils import (
    limpar_tela,
    mensagem_aviso,
    pausar,
)

from src.avedex.catalogo import (
    listar_aves,
    buscar_aves,
    tela_busca,
    selecionar_ave_por_id,
    escolher_ave,
    mostrar_ave_aleatoria,
)

from src.avedex.comparacao import tela_comparacao

from src.avedex.batalha import batalha_avedex

from src.avedex.multimidia import (
    visualizar_imagem,
    tocar_som,
)


def selecionar_e_visualizar_imagem(catalogo):
    ave = escolher_ave(
        catalogo,
        "Escolha uma ave para visualizar a imagem"
    )

    if ave is not None:
        visualizar_imagem(ave)


def selecionar_e_tocar_som(catalogo):
    ave = escolher_ave(
        catalogo,
        "Escolha uma ave para ouvir o som"
    )

    if ave is not None:
        tocar_som(ave)


def processar_opcao(opcao, catalogo):
    if opcao == "1":
        listar_aves(catalogo)
        pausar()

    elif opcao == "2":
        tela_busca(catalogo)
        pausar()

    elif opcao == "3":
        mostrar_ave_aleatoria(catalogo)
        pausar()

    elif opcao == "4":
        selecionar_ave_por_id(catalogo)
        pausar()

    elif opcao == "5":
        tela_comparacao(catalogo)
        pausar()

    elif opcao == "6":
        batalha_avedex(catalogo)
        pausar()

    elif opcao == "7":
        selecionar_e_visualizar_imagem(catalogo)
        pausar()

    elif opcao == "8":
        selecionar_e_tocar_som(catalogo)
        pausar()

    elif opcao == "9":
        verificar_ambiente()
        pausar()

    elif opcao == "10":
        mostrar_creditos()
        pausar()

    elif opcao == "0":
        limpar_tela()
        print("Obrigado por usar a AveDex!")

    else:
        mensagem_aviso("Opção inválida.")
        pausar()


def executar():
    catalogo_aves = carregar_aves()

    problemas = validar_dataset(catalogo_aves)

    if problemas:
        mensagem_aviso(
            "O dataset possui problemas:"
        )

        for problema in problemas:
            print(f"- {problema}")

        pausar()

    if not catalogo_aves:
        mensagem_aviso(
            "Nenhuma ave foi carregada."
        )
        return

    abertura(catalogo_aves)

    while True:
        exibir_menu_principal()

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        processar_opcao(
            opcao,
            catalogo_aves
        )

        if opcao == "0":
            break