from datetime import datetime

from config import PEDIDOS

from aprendizado.memoria import (
    carregar_memoria,
    salvar_memoria
)

from negocio.produtos import buscar_preco

from negocio.estoque import (
    retirar_item,
    quantidade_disponivel
)



CUSTO_PASTEL = 5.00



def carregar_pedidos():

    pedidos = carregar_memoria(
        PEDIDOS
    )

    if not isinstance(
        pedidos,
        list
    ):
        pedidos = []

    return pedidos



def salvar_pedidos(pedidos):

    salvar_memoria(
        PEDIDOS,
        pedidos
    )



def criar_pedido(cliente, produto, quantidade):


    preco = buscar_preco(
        produto
    )


    if preco is None:

        return None



    estoque = quantidade_disponivel(
        produto
    )


    if estoque < quantidade:

        return {

            "erro": "Estoque insuficiente",

            "disponivel": estoque

        }



    total = preco * quantidade


    custo = CUSTO_PASTEL * quantidade


    lucro = total - custo



    pedido = {


        "cliente": cliente,


        "produto": produto,


        "quantidade": quantidade,


        "valor_unitario": preco,


        "total": total,


        "custo": custo,


        "lucro": lucro,


        "data": datetime.now().strftime(
            "%d/%m/%Y"
        )

    }



    pedidos = carregar_pedidos()



    pedidos.append(
        pedido
    )



    salvar_pedidos(
        pedidos
    )



    retirar_item(
        produto,
        quantidade
    )



    return pedido



def listar_pedidos():

    return carregar_pedidos()



def apagar_todos_pedidos():


    salvar_pedidos(
        []
    )


    return True



def apagar_pedidos_periodo(periodo):

    pedidos = carregar_pedidos()


    hoje = datetime.now()


    novos = []



    for pedido in pedidos:


        data = datetime.strptime(
            pedido["data"],
            "%d/%m/%Y"
        )



        manter = True



        if periodo == "hoje":

            if data.date() == hoje.date():

                manter = False



        elif periodo == "mes":


            if (
                data.month == hoje.month
                and data.year == hoje.year
            ):

                manter = False



        if manter:

            novos.append(
                pedido
            )



    salvar_pedidos(
        novos
    )


    return True



def buscar_pedidos_cliente(cliente):

    pedidos = carregar_pedidos()


    resultado = []



    for pedido in pedidos:


        if pedido["cliente"].lower() == cliente.lower():

            resultado.append(
                pedido
            )


    return resultado