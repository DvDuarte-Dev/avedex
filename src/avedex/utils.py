import unicodedata

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