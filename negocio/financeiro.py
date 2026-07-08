from datetime import datetime

from config import PEDIDOS, GASTOS

from aprendizado.memoria import (
    carregar_memoria,
    salvar_memoria
)



def carregar_pedidos():

    pedidos = carregar_memoria(PEDIDOS)

    if not isinstance(pedidos, list):
        pedidos = []

    return pedidos



def carregar_gastos():

    gastos = carregar_memoria(GASTOS)

    if not isinstance(gastos, list):
        gastos = []

    return gastos



def registrar_gasto(descricao, valor):

    gastos = carregar_gastos()

    gastos.append(
        {
            "descricao": descricao,
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y")
        }
    )

    salvar_memoria(
        GASTOS,
        gastos
    )

    return True



def filtrar_periodo(lista, periodo):

    hoje = datetime.now()

    resultado = []


    for item in lista:

        try:

            data = datetime.strptime(
                item["data"],
                "%d/%m/%Y"
            )

        except:

            continue


        if periodo == "hoje":

            if data.date() == hoje.date():

                resultado.append(item)


        elif periodo == "semana":

            diferenca = (
                hoje.date()
                -
                data.date()
            ).days

            if diferenca <= 7:

                resultado.append(item)


        elif periodo == "mes":

            if (
                data.month == hoje.month
                and data.year == hoje.year
            ):

                resultado.append(item)


    return resultado



def calcular_financeiro(periodo="total"):

    pedidos = carregar_pedidos()

    gastos = carregar_gastos()


    if periodo != "total":

        pedidos = filtrar_periodo(
            pedidos,
            periodo
        )

        gastos = filtrar_periodo(
            gastos,
            periodo
        )


    vendas = sum(
        pedido.get("total", 0)
        for pedido in pedidos
    )


    custos = sum(
        pedido.get("custo", 0)
        for pedido in pedidos
    )


    gastos_extras = sum(
        gasto.get("valor", 0)
        for gasto in gastos
    )


    lucro = (
        vendas
        -
        custos
        -
        gastos_extras
    )


    quantidade = sum(
        pedido.get("quantidade", 0)
        for pedido in pedidos
    )


    return {

        "vendas": vendas,

        "gastos": custos + gastos_extras,

        "lucro": lucro,

        "quantidade": quantidade

    }



def zerar_vendas():

    salvar_memoria(
        PEDIDOS,
        []
    )

    return True



def zerar_gastos():

    salvar_memoria(
        GASTOS,
        []
    )

    return True