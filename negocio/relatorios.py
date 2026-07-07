from negocio.financeiro import calcular_financeiro
from negocio.pedidos import listar_pedidos
from negocio.pagamentos import listar_devedores



def resumo_texto():

    financeiro = calcular_financeiro()

    pedidos = listar_pedidos()

    devedores = listar_devedores()


    quantidade = sum(
        p["quantidade"]
        for p in pedidos
    )


    return f"""
📊 Relatório PastelIA

🥟 Pastéis vendidos:
{quantidade}

💰 Faturamento:
R$ {financeiro['vendas']:.2f}

📦 Gastos:
R$ {financeiro['gastos']:.2f}

📈 Lucro:
R$ {financeiro['lucro']:.2f}

👥 Clientes devendo:
{len(devedores)}
"""