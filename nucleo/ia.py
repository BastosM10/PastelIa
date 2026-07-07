import re

from nucleo.intencoes import identificar_intencao

from aprendizado.aprender import aprender

from negocio.pedidos import criar_pedido

from negocio.pagamentos import (
    registrar_divida,
    listar_devedores,
    registrar_pagamento
)

from negocio.relatorios import resumo_texto
from negocio.produtos import listar_produtos
from negocio.estoque import ver_estoque



def processar_pedido(mensagem):

    texto = mensagem.lower()


    cliente = None
    quantidade = None


    # Exemplos:
    # anota para João 3
    # coloca Maria Souza 5
    # pedido para Carlos 2

    padrao1 = re.search(
        r"(?:anota|coloca|reserva|pedido)\s+(?:para|pro|pra)\s+(.+?)\s+(\d+)",
        texto
    )


    # Exemplos:
    # João 3 anotado
    # Maria Souza 2 pastéis

    padrao2 = re.search(
        r"(.+?)\s+(\d+)\s*(?:anotado|anota|past[eé]is)?",
        texto
    )


    if padrao1:

        cliente = padrao1.group(1).strip()
        quantidade = int(padrao1.group(2))


    elif padrao2:

        cliente = padrao2.group(1).strip()
        quantidade = int(padrao2.group(2))


    if cliente and quantidade:


        pedido = criar_pedido(
            cliente,
            "pastel",
            quantidade
        )


        if pedido is None:

            return "Não encontrei o produto."


        resposta = (
            "✅ Pedido registrado!\n\n"
            f"👤 Cliente: {cliente.title()}\n"
            f"🥟 Quantidade: {quantidade} pastéis\n"
            f"💰 Total: R$ {pedido['total']:.2f}"
        )


        # anotado significa que ficou devendo

        if (
            "fiado" in texto
            or "devendo" in texto
            or "anotado" in texto
            or "pendente" in texto
        ):

            registrar_divida(
                cliente,
                pedido["total"]
            )

            resposta += "\n⚠️ Registrado como pendente."


        return resposta


    return "Não consegui identificar o pedido."



def responder(mensagem):

    texto = mensagem.lower()



    # Pagamento

    if "pagou" in texto:

        cliente = texto.replace(
            "pagou",
            ""
        ).strip()


        if registrar_pagamento(cliente):

            return "✅ Pagamento registrado."


        return "Não encontrei essa dívida."



    intencao = identificar_intencao(mensagem)



    if intencao == "cumprimento":

        return "Olá! Sou a PastelIA 🤖"



    if intencao == "pedido":

        return processar_pedido(mensagem)



    if intencao == "dividas":

        dados = listar_devedores()


        if not dados:

            return "✅ Ninguém está devendo."


        resposta = "📋 CLIENTES DEVENDO\n\n"
        resposta += "Cliente | Valor\n"
        resposta += "----------------\n"


        total = 0


        for cliente, valor in dados.items():

            resposta += (
                f"{cliente.title()} | R$ {valor:.2f}\n"
            )

            total += valor


        resposta += "----------------\n"
        resposta += f"Total: R$ {total:.2f}"


        return resposta



    if intencao == "relatorio":

        return resumo_texto()



    if intencao == "produto":

        return str(listar_produtos())



    if intencao == "estoque":

        return str(ver_estoque())



    if intencao == "aprendizado":

        return aprender(mensagem)



    return "Ainda não entendi."