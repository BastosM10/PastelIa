from config import PAGAMENTOS
from aprendizado.memoria import (
    carregar_memoria,
    salvar_memoria
)



def carregar_pagamentos():

    pagamentos = carregar_memoria(
        PAGAMENTOS
    )

    if not isinstance(
        pagamentos,
        list
    ):
        pagamentos = []

    return pagamentos



def registrar_divida(cliente, valor):

    pagamentos = carregar_pagamentos()


    divida = {

        "cliente": cliente,

        "valor": valor,

        "status": "pendente"

    }


    pagamentos.append(
        divida
    )


    salvar_memoria(
        PAGAMENTOS,
        pagamentos
    )


    return divida



def registrar_pagamento(cliente):

    pagamentos = carregar_pagamentos()

    encontrou = False


    for pagamento in pagamentos:

        if (
            pagamento["cliente"].lower()
            == cliente.lower()
            and pagamento["status"]
            == "pendente"
        ):

            pagamento["status"] = "pago"

            encontrou = True



    salvar_memoria(
        PAGAMENTOS,
        pagamentos
    )


    return encontrou



def listar_devedores():

    pagamentos = carregar_pagamentos()

    devedores = {}



    for pagamento in pagamentos:


        if pagamento.get(
            "status"
        ) == "pendente":


            cliente = pagamento["cliente"]


            valor = pagamento["valor"]



            if cliente in devedores:

                devedores[cliente] += valor

            else:

                devedores[cliente] = valor



    return devedores



def apagar_todas_dividas():

    """
    Marca todas as dívidas pendentes como pagas.
    """

    pagamentos = carregar_pagamentos()



    for pagamento in pagamentos:


        if pagamento.get(
            "status"
        ) == "pendente":

            pagamento["status"] = "pago"



    salvar_memoria(
        PAGAMENTOS,
        pagamentos
    )


    return True



def remover_divida_cliente(cliente):

    pagamentos = carregar_pagamentos()

    encontrou = False



    for pagamento in pagamentos:


        if pagamento["cliente"].lower() == cliente.lower():


            pagamento["status"] = "pago"

            encontrou = True



    salvar_memoria(
        PAGAMENTOS,
        pagamentos
    )


    return encontrou



def total_a_receber():

    devedores = listar_devedores()


    return sum(
        devedores.values()
    )