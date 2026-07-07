import json
import os


def carregar_memoria(caminho):

    if not os.path.exists(caminho):
        return {}

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except:
        return {}



def salvar_memoria(caminho, dados):

    pasta = os.path.dirname(caminho)

    if not os.path.exists(pasta):
        os.makedirs(pasta)


    with open(caminho, "w", encoding="utf-8") as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# compatibilidade
carregar = carregar_memoria
salvar = salvar_memoria