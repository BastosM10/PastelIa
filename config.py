import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PASTA_DADOS = os.path.join(BASE_DIR, "dados")


MEMORIA = os.path.join(PASTA_DADOS, "memoria.json")
PEDIDOS = os.path.join(PASTA_DADOS, "pedidos.json")
PAGAMENTOS = os.path.join(PASTA_DADOS, "pagamentos.json")
VENDAS = os.path.join(PASTA_DADOS, "vendas.json")
GASTOS = os.path.join(PASTA_DADOS, "gastos.json")
ESTOQUE = os.path.join(PASTA_DADOS, "estoque.json")


NOME_IA = "PastelIA"
VERSAO = "1.0"
PRECO_PASTEL = 8.00