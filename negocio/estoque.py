from config import ESTOQUE

from aprendizado.memoria import (
    carregar_memoria,
    salvar_memoria
)


ESTOQUE_INICIAL = 30



def ver_estoque():

    estoque = carregar_memoria(
        ESTOQUE
    )


    if not isinstance(
        estoque,
        dict
    ):

        estoque = {
            "pastel": 0
        }


    return estoque



def iniciar_venda():

    estoque = ver_estoque()

    estoque["pastel"] = ESTOQUE_INICIAL


    salvar_memoria(
        ESTOQUE,
        estoque
    )


    return estoque



def adicionar_item(nome, quantidade):

    estoque = ver_estoque()


    estoque[nome] = (
        estoque.get(nome, 0)
        +
        quantidade
    )


    salvar_memoria(
        ESTOQUE,
        estoque
    )


    return estoque



def definir_estoque(nome, quantidade):

    """
    Define exatamente a quantidade informada.
    Exemplo:
    "Ainda tenho 20 pastéis"
    """

    estoque = ver_estoque()


    estoque[nome] = quantidade


    salvar_memoria(
        ESTOQUE,
        estoque
    )


    return estoque



def retirar_item(nome, quantidade):

    estoque = ver_estoque()


    disponivel = estoque.get(
        nome,
        0
    )


    if disponivel < quantidade:

        return {
            "erro": "estoque_insuficiente",
            "disponivel": disponivel
        }


    estoque[nome] = (
        disponivel
        -
        quantidade
    )


    salvar_memoria(
        ESTOQUE,
        estoque
    )


    return estoque



def quantidade_disponivel(nome):

    estoque = ver_estoque()


    return estoque.get(
        nome,
        0
    )



def resumo_estoque():

    estoque = ver_estoque()


    resposta = "📦 Estoque atual:\n\n"


    for item, quantidade in estoque.items():

        resposta += (
            f"🥟 {item}: "
            f"{quantidade}\n"
        )


    return resposta



def limpar_estoque():

    salvar_memoria(
        ESTOQUE,
        {}
    )


    return True