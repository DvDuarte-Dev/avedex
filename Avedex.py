import unicodedata

LARGURA_COLUNA = 25
TAMANHO_LINHA = 50
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

def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto

def valor_ou_indisponivel(valor, unidade=""):
    if valor is None:
        return "Não informado"

    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)

def cortar_texto(texto, tamanho=25):
    if texto is None:
        return "Não informado"

    texto = str(texto).strip()

    if len(texto) <= tamanho:
        return texto

    return texto[: tamanho - 3] + "..."

def preparar_valor_comparacao(ave, campo, unidade):
    valor = ave.get(campo)

    if campo == "habitat":
        return cortar_texto(valor, 25)

    return valor_ou_indisponivel(valor, unidade)

def imprimir_linha_comparacao(rotulo, valor1, valor2):
    valor1 = valor_ou_indisponivel(valor1)
    valor2 = valor_ou_indisponivel(valor2)

    print(
        f"{rotulo:<{LARGURA_COLUNA}}"
        f"{str(valor1):<{LARGURA_COLUNA}}"
        f"{str(valor2):<{LARGURA_COLUNA}}"
    )

def comparar_aves(ave1, ave2):
    exibir_titulo("COMPARAÇÃO DE AVES")

    print(
        f"{'Característica':<{LARGURA_COLUNA}}"
        f"{ave1['nome_popular']:<{LARGURA_COLUNA}}"
        f"{ave2['nome_popular']:<{LARGURA_COLUNA}}"
    )

    print("-" * TAMANHO_SEPARADOR)

    for rotulo, campo, unidade in CAMPOS_COMPARACAO:
        valor1 = preparar_valor_comparacao(ave1, campo, unidade)
        valor2 = preparar_valor_comparacao(ave2, campo, unidade)

        imprimir_linha_comparacao(
            rotulo,
            valor1,
            valor2
        )

    print()
    exibir_linha()

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
        print("As duas aves possuem o mesmo peso.")

def tela_comparacao(catalogo):
    exibir_titulo("COMPARAÇÃO DE AVES")

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
        print("Escolha duas aves diferentes.")
        return

    comparar_aves(ave1, ave2)

def exibir_linha():
    print("=" * TAMANHO_LINHA)

def exibir_titulo(titulo):
    print()
    exibir_linha()
    print(titulo)
    exibir_linha()

def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    exibir_titulo("AVEDEX - MENU PRINCIPAL")

    for opcao in OPCOES_MENU:
        print(opcao)

def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def listar_aves(catalogo):
    exibir_titulo("AVES CADASTRADAS")

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
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

    id_escolhido = input(
        "\nDigite o ID da ave: "
    ).strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)

def escolher_ave(catalogo, mensagem):
    listar_aves(catalogo)

    id_escolhido = input(f"\n{mensagem}: ").strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None

    return ave_encontrada


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves.")
    print("O projeto evolui durante a disciplina de Boas Práticas.")
    print("Futuramente teremos busca, comparação e testes.")

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

catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",

        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "id": 2,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos, áreas abertas e ambientes rurais",

        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "O macho possui plumagem amarela intensa."
    },
    {
        "id": 3,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",

        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Insetos e outros pequenos invertebrados",
        "curiosidade": "Constrói um ninho de barro característico."
    },
    {
        "id": 4,
        "nome_popular": "Sabiá-laranjeira",
        "nome_cientifico": "Turdus rufiventris",
        "ordem": "Passeriformes",
        "familia": "Turdidae",
        "dieta_tipo": "Onívora",
        "habitat": "Jardins, parques e áreas arborizadas",

        "comprimento_cm": 25,
        "peso_g": 77,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Frutas, insetos e minhocas",
        "curiosidade": "É considerada a ave símbolo do Brasil."
    },
    {
        "id": 5,
        "nome_popular": "Tucano-toco",
        "nome_cientifico": "Ramphastos toco",
        "ordem": "Piciformes",
        "familia": "Ramphastidae",
        "dieta_tipo": "Onívora",
        "habitat": "Cerrado, matas abertas e regiões arborizadas",

        "comprimento_cm": 61,
        "peso_g": 650,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Frutas, ovos e pequenos animais",
        "curiosidade": "Possui um dos maiores bicos entre as aves."
    },
    {
        "id": 6,
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Granívora",
        "habitat": "Pantanal e Cerrado",

        "comprimento_cm": 100,
        "peso_g": 1400,
        "status_conservacao": "Vulnerável",
        "indice_conservacao": 3,

        "alimentacao": "Frutas e sementes",
        "curiosidade": "É a maior espécie de arara do mundo."
    },
    {
        "id": 7,
        "nome_popular": "Coruja-buraqueira",
        "nome_cientifico": "Athene cunicularia",
        "ordem": "Strigiformes",
        "familia": "Strigidae",
        "dieta_tipo": "Carnívora",
        "habitat": "Campos e áreas abertas",

        "comprimento_cm": 24,
        "peso_g": 170,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Insetos e pequenos vertebrados",
        "curiosidade": "Costuma viver em tocas no chão."
    },
    {
        "id": 8,
        "nome_popular": "Beija-flor-tesoura",
        "nome_cientifico": "Eupetomena macroura",
        "ordem": "Apodiformes",
        "familia": "Trochilidae",
        "dieta_tipo": "Nectarívora",
        "habitat": "Jardins, matas e áreas urbanas",

        "comprimento_cm": 16,
        "peso_g": 7,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Néctar e pequenos insetos",
        "curiosidade": "Pode bater as asas mais de 50 vezes por segundo."
    },
    {
        "id": 9,
        "nome_popular": "Garça-branca-grande",
        "nome_cientifico": "Ardea alba",
        "ordem": "Pelecaniformes",
        "familia": "Ardeidae",
        "dieta_tipo": "Carnívora",
        "habitat": "Lagos, rios e áreas alagadas",

        "comprimento_cm": 98,
        "peso_g": 1000,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": "Peixes, anfíbios e pequenos animais",
        "curiosidade": "É uma excelente pescadora e caça parada na água."
    }
]

exibir_linha()
print("AVEDEX")
exibir_linha()

nome_usuario = input(
    "Digite seu nome: "
).strip()

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