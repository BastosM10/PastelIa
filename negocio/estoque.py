from config import ESTOQUE
from aprendizado.memoria import carregar_memoria, salvar_memoria



def ver_estoque():

    estoque = carregar_memoria(ESTOQUE)

    if not isinstance(estoque, dict):
        estoque = {}

    return estoque



def adicionar_item(nome, quantidade):

    estoque = ver_estoque()


    estoque[nome] = estoque.get(nome, 0) + quantidade


    salvar_memoria(
        ESTOQUE,
        estoque
    )


    return estoque



def retirar_item(nome, quantidade):

    estoque = ver_estoque()


    if nome in estoque:

        estoque[nome] -= quantidade


    salvar_memoria(
        ESTOQUE,
        estoque
    )


    return estoque