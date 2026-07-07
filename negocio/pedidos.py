from datetime import datetime

from config import PEDIDOS
from aprendizado.memoria import carregar_memoria, salvar_memoria
from negocio.produtos import buscar_preco



def carregar_pedidos():

    pedidos = carregar_memoria(PEDIDOS)

    if not isinstance(pedidos, list):
        pedidos = []

    return pedidos



def criar_pedido(cliente, produto, quantidade):

    preco = buscar_preco(produto)

    if preco is None:
        return None


    pedido = {
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
        "valor_unitario": preco,
        "total": preco * quantidade,
        "data": datetime.now().strftime("%d/%m/%Y")
    }


    pedidos = carregar_pedidos()

    pedidos.append(pedido)

    salvar_memoria(
        PEDIDOS,
        pedidos
    )


    return pedido



def listar_pedidos():

    return carregar_pedidos()