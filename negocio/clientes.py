from config import CLIENTES
from aprendizado.memoria import carregar, salvar


def carregar_clientes():
    return carregar(CLIENTES)



def adicionar_cliente(nome):

    clientes = carregar_clientes()

    nome = nome.lower()

    if nome not in clientes:
        clientes.append(nome)
        salvar(CLIENTES, clientes)

    return clientes



def listar_clientes():

    return carregar_clientes()