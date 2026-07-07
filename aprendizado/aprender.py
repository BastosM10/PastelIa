from config import MEMORIA
from aprendizado.memoria import carregar_memoria, salvar_memoria



def aprender(frase):

    memoria = carregar_memoria(MEMORIA)


    if "aprenda" not in frase.lower():

        return None


    conteudo = frase.lower().replace(
        "aprenda",
        ""
    ).strip()


    if "=" in conteudo:

        pergunta, resposta = conteudo.split(
            "=",
            1
        )


        memoria[pergunta.strip()] = resposta.strip()


        salvar_memoria(
            MEMORIA,
            memoria
        )


        return "Aprendi essa informação."


    return "Não consegui aprender."