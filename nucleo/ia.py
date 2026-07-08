import re

from nucleo.intencoes import identificar_intencao

from aprendizado.aprender import aprender

from negocio.pedidos import (
    criar_pedido,
    apagar_todos_pedidos
)

from negocio.pagamentos import (
    registrar_divida,
    listar_devedores,
    registrar_pagamento,
    apagar_todas_dividas
)

from negocio.relatorios import resumo_texto

from negocio.produtos import listar_produtos

from negocio.estoque import (
    ver_estoque,
    definir_estoque
)



def limpar_nome(nome):

    nome = nome.lower()


    palavras = [
        "anota",
        "anotado",
        "anotei",
        "fiado",
        "pastel",
        "pastéis",
        "pasteis",
        "pedido",
        "pegou",
        "leva",
        "levou",
        "para",
        "pra",
        "pro"
    ]


    for palavra in palavras:

        nome = nome.replace(
            palavra,
            " "
        )


    nome = re.sub(
        r"\s+",
        " ",
        nome
    )


    return nome.strip()



def extrair_pedido(texto):

    texto = texto.lower()


    numeros = re.findall(
        r"\d+",
        texto
    )


    quantidade = None


    if numeros:

        quantidade = int(
            numeros[0]
        )


    cliente = texto


    cliente = re.sub(
        r"\d+",
        " ",
        cliente
    )


    cliente = limpar_nome(
        cliente
    )


    return cliente, quantidade



def extrair_cliente_pagamento(texto):

    texto = texto.lower()


    for palavra in [
        "pagou",
        "paguei",
        "pago",
        "quitou",
        "acertou",
        "pix"
    ]:

        texto = texto.replace(
            palavra,
            " "
        )


    return limpar_nome(
        texto
    )



def processar_pedido(mensagem):

    cliente, quantidade = extrair_pedido(
        mensagem
    )


    if not cliente or not quantidade:

        return "Não consegui entender o pedido."



    pedido = criar_pedido(
        cliente,
        "pastel",
        quantidade
    )



    if pedido is None:

        return "Produto não encontrado."



    if "erro" in pedido:

        return (
            "⚠️ Estoque insuficiente.\n"
            f"Disponível: {pedido['disponivel']}"
        )



    resposta = (
        "✅ Pedido registrado!\n\n"
        f"👤 Cliente: {cliente.title()}\n"
        f"🥟 Quantidade: {quantidade} pastéis\n"
        f"💰 Total: R$ {pedido['total']:.2f}"
    )



    if any(
        palavra in mensagem.lower()
        for palavra in [
            "anota",
            "anotado",
            "anotei",
            "fiado",
            "devendo",
            "pendente"
        ]
    ):

        registrar_divida(
            cliente,
            pedido["total"]
        )


        resposta += (
            "\n⚠️ Registrado como fiado."
        )



    return resposta



def responder(mensagem):

    texto = mensagem.lower()



    # Atualizar estoque

    if (
        ("tenho" in texto or
         "ainda tenho" in texto or
         "estou com" in texto)
        and
        ("pastel" in texto or
         "pastéis" in texto or
         "pasteis" in texto)
    ):


        numeros = re.findall(
            r"\d+",
            texto
        )


        if numeros:

            quantidade = int(
                numeros[0]
            )


            definir_estoque(
                "pastel",
                quantidade
            )


            return (
                "✅ Estoque atualizado!\n\n"
                f"🥟 Pastéis disponíveis: {quantidade}"
            )



    intencao = identificar_intencao(
        mensagem
    )



    if intencao == "cumprimento":

        return (
            "Olá! Sou a PastelIA 🤖🥟\n"
            "Como posso ajudar?"
        )



    if intencao == "pedido":

        return processar_pedido(
            mensagem
        )



    if intencao == "pagamento":

        cliente = extrair_cliente_pagamento(
            mensagem
        )


        if registrar_pagamento(cliente):

            return "✅ Pagamento registrado."


        return "Não encontrei essa dívida."



    if intencao == "dividas":

        dados = listar_devedores()


        if not dados:

            return "✅ Ninguém está devendo."


        resposta = "📋 CLIENTES DEVENDO\n\n"

        total = 0


        for cliente, valor in dados.items():

            resposta += (
                f"👤 {cliente.title()}: "
                f"R$ {valor:.2f}\n"
            )

            total += valor


        resposta += (
            f"\n💰 Total a receber: R$ {total:.2f}"
        )


        return resposta



    if intencao == "apagar_dividas":

        apagar_todas_dividas()

        return "✅ Todas as dívidas foram apagadas."



    if intencao == "zerar_vendas":

        apagar_todos_pedidos()

        return "✅ Vendas zeradas."



    if intencao == "relatorio":

        if "hoje" in texto:

            return resumo_texto("hoje")


        if "semana" in texto:

            return resumo_texto("semana")


        if "mes" in texto:

            return resumo_texto("mes")


        return resumo_texto()



    if intencao == "estoque":

        return str(
            ver_estoque()
        )



    if intencao == "produto":

        return str(
            listar_produtos()
        )



    if intencao == "aprendizado":

        return aprender(
            mensagem
        )



    return "Ainda não entendi 🤔"