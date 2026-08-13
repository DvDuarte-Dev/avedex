OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ave aleatória",
    "4 - Ver detalhes de uma ave",
    "5 - Comparar duas aves",
    "6 - Batalha AveDex",
    "7 - Verificar ambiente",
    "8 - Créditos e fontes",
    "0 - Sair",
]

TAMANHO_LINHA = 50

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

def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves.")
    print("O projeto evolui durante a disciplina de Boas Práticas.")
    print("Futuramente teremos busca, comparação e testes.")