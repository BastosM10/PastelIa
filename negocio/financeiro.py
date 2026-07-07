from config import VENDAS, GASTOS
from aprendizado.memoria import carregar_memoria, salvar_memoria



def registrar_venda(valor):

    vendas = carregar_memoria(VENDAS)

    if not isinstance(vendas, list):
        vendas = []


    vendas.append(valor)

    salvar_memoria(
        VENDAS,
        vendas
    )



def registrar_gasto(descricao, valor):

    gastos = carregar_memoria(GASTOS)

    if not isinstance(gastos, list):
        gastos = []


    gastos.append(
        {
            "descricao": descricao,
            "valor": valor
        }
    )


    salvar_memoria(
        GASTOS,
        gastos
    )



def calcular_financeiro():

    vendas = carregar_memoria(VENDAS)

    gastos = carregar_memoria(GASTOS)


    total_vendas = sum(vendas)

    total_gastos = sum(
        item["valor"]
        for item in gastos
    )


    return {
        "vendas": total_vendas,
        "gastos": total_gastos,
        "lucro": total_vendas - total_gastos
    }