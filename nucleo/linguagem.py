def limpar_texto(texto):
    return texto.lower().strip()


def palavras_chave(texto):
    texto = limpar_texto(texto)
    return texto.split()