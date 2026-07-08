import json
import os
import shutil
from datetime import datetime



def criar_backup(caminho):

    if not os.path.exists(caminho):

        return


    backup = (
        caminho
        +
        ".backup"
    )


    try:

        shutil.copy(
            caminho,
            backup
        )

    except:

        pass



def carregar_memoria(caminho):

    if not os.path.exists(caminho):

        return {}


    try:

        with open(
            caminho,
            "r",
            encoding="utf-8"
        ) as arquivo:


            dados = json.load(
                arquivo
            )


            return dados



    except:

        return {}



def salvar_memoria(caminho, dados):


    pasta = os.path.dirname(
        caminho
    )


    if pasta and not os.path.exists(
        pasta
    ):

        os.makedirs(
            pasta
        )



    # cria backup antes de alterar

    criar_backup(
        caminho
    )



    try:


        with open(
            caminho,
            "w",
            encoding="utf-8"
        ) as arquivo:


            json.dump(

                dados,

                arquivo,

                indent=4,

                ensure_ascii=False

            )



    except Exception as erro:


        print(
            "Erro salvando memória:",
            erro
        )



def adicionar_historico(caminho, evento):


    historico = carregar_memoria(
        caminho
    )


    if not isinstance(
        historico,
        list
    ):

        historico = []



    historico.append({

        "evento": evento,

        "data": datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )

    })



    salvar_memoria(
        caminho,
        historico
    )



# compatibilidade

carregar = carregar_memoria

salvar = salvar_memoria