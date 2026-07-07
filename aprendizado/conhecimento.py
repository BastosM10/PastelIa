from aprendizado.memoria import (
    carregar_conhecimento,
    salvar_conhecimento
)


def adicionar_conhecimento(chave, valor):

    conhecimento = carregar_conhecimento()

    conhecimento[chave] = valor

    salvar_conhecimento(conhecimento)


def buscar_conhecimento(chave):

    conhecimento = carregar_conhecimento()

    return conhecimento.get(chave)