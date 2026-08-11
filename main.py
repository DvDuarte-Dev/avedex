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
)

from src.avedex.interface import (
    exibir_linha,
    exibir_titulo,
    pausar,
    exibir_menu,
    mostrar_boas_vindas,
    mostrar_sobre,
)

from src.avedex.utils import (
    normalizar_texto,
    valor_ou_indisponivel,
    cortar_texto,
)

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