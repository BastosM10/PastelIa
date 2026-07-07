def identificar_intencao(mensagem):

    texto = mensagem.lower()


    if any(p in texto for p in ["oi", "olá", "ola", "bom dia"]):
        return "cumprimento"


    if any(p in texto for p in ["anota", "pedido", "pastel"]):
        return "pedido"


    if any(p in texto for p in ["devendo", "dívida", "divida"]):
        return "dividas"


    if "pagou" in texto:
        return "pagamento"


    if any(p in texto for p in ["relatório", "relatorio", "vendas", "lucro"]):
        return "relatorio"


    if "estoque" in texto:
        return "estoque"


    if "produto" in texto:
        return "produto"


    if "aprenda" in texto:
        return "aprendizado"


    return "desconhecido"