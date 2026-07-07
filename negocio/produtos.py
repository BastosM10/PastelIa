from config import PRECO_PASTEL


def listar_produtos():

    return {
        "pastel": PRECO_PASTEL
    }



def buscar_preco(produto):

    produtos = listar_produtos()

    return produtos.get(produto.lower())