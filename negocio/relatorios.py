from negocio.financeiro import calcular_financeiro
from negocio.pagamentos import listar_devedores
from negocio.estoque import ver_estoque



def resumo_texto(periodo="total"):

    financeiro = calcular_financeiro(periodo)

    devedores = listar_devedores()

    estoque = ver_estoque()


    resposta = "📊 Relatório PastelIA\n\n"


    resposta += (
        f"🥟 Pastéis vendidos: "
        f"{financeiro['quantidade']}\n\n"
    )


    resposta += (
        f"💰 Faturamento: "
        f"R$ {financeiro['vendas']:.2f}\n\n"
    )


    resposta += (
        f"📦 Gastos: "
        f"R$ {financeiro['gastos']:.2f}\n\n"
    )


    resposta += (
        f"📈 Lucro: "
        f"R$ {financeiro['lucro']:.2f}\n\n"
    )


    resposta += (
        f"👥 Clientes devendo: "
        f"{len(devedores)}\n\n"
    )


    if estoque:

        resposta += "📦 Estoque atual:\n"

        for item, quantidade in estoque.items():

            resposta += (
                f"{item}: {quantidade}\n"
            )


    return resposta