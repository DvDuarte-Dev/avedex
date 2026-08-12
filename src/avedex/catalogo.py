from src.avedex.interface import exibir_titulo
from src.avedex.utils import normalizar_texto
from src.avedex.utils import mensagem_aviso

def listar_aves(catalogo):
    exibir_titulo("AVES CADASTRADAS")

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")

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
    listar_aves(catalogo)

    id_escolhido = ler_id_ave(
        "\nDigite o ID da ave: "
    )

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso(
            "Ave não encontrada. Confira o ID informado."
        )
    else:
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