import re



def normalizar(texto):

    texto = texto.lower()

    substituicoes = {
        "á": "a",
        "à": "a",
        "ã": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u"
    }


    for antigo, novo in substituicoes.items():

        texto = texto.replace(
            antigo,
            novo
        )


    return texto.strip()



def possui(texto, palavras):

    return any(
        palavra in texto
        for palavra in palavras
    )



def identificar_intencao(mensagem):

    texto = normalizar(
        mensagem
    )



    # =====================
    # ATUALIZAR ESTOQUE
    # =====================

    if (
        re.search(r"\d+", texto)
        and
        possui(texto, [
            "tenho",
            "ainda tenho",
            "estou com",
            "sobrou",
            "coloca",
            "coloque",
            "atualiza",
            "corrige"
        ])
        and
        possui(texto, [
            "pastel",
            "estoque"
        ])
    ):

        return "atualizar_estoque"



    # =====================
    # CUMPRIMENTO
    # =====================

    if possui(texto, [
        "oi",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite",
        "fala"
    ]):

        return "cumprimento"



    # =====================
    # APAGAR
    # =====================

    if possui(texto, [
        "apaga",
        "apague",
        "limpa",
        "zera",
        "zerar",
        "remove"
    ]):


        if possui(texto, [
            "divida",
            "dividas",
            "devedor",
            "devedores",
            "fiado"
        ]):

            return "apagar_dividas"



        if possui(texto, [
            "venda",
            "vendas"
        ]):

            return "zerar_vendas"



    # =====================
    # PAGAMENTO
    # =====================

    if possui(texto, [
        "pagou",
        "paguei",
        "quitou",
        "acertou",
        "fez o pix",
        "mandou dinheiro"
    ]):

        return "pagamento"



    # =====================
    # DIVIDAS
    # =====================

    if possui(texto, [
        "quem deve",
        "quem esta devendo",
        "quem ta devendo",
        "devedores",
        "divida",
        "dividas",
        "fiado",
        "pendente"
    ]):

        return "dividas"



    # =====================
    # RELATORIOS
    # =====================

    if possui(texto, [
        "lucro",
        "relatorio",
        "relatório",
        "resumo",
        "quanto vendi",
        "quanto entrou",
        "quanto fiz",
        "faturamento",
        "balanco"
    ]):

        return "relatorio"



    # =====================
    # ESTOQUE
    # =====================

    if possui(texto, [
        "estoque",
        "quanto tem",
        "quantos tenho",
        "quanto resta"
    ]):

        return "estoque"



    # =====================
    # PRODUTOS
    # =====================

    if possui(texto, [
        "produto",
        "preco",
        "preço",
        "cardapio",
        "cardápio"
    ]):

        return "produto"



    # =====================
    # PEDIDOS COM PALAVRAS
    # =====================

    if possui(texto, [
        "anota",
        "anotado",
        "anotei",
        "pedido",
        "pastel",
        "pastéis",
        "quero",
        "separa"
    ]):

        return "pedido"



    # =====================
    # PEDIDO SIMPLES
    # Ex: 3 pro João
    # =====================

    if re.search(
        r"\d+",
        texto
    ):

        return "pedido"



    return "desconhecido"