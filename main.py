from nucleo.ia import responder


print("🤖 PastelIA iniciada!")
print("Digite 'sair' para fechar.")


while True:

    mensagem = input("\nVocê: ")


    if mensagem.lower() == "sair":
        print("PastelIA encerrada.")
        break


    resposta = responder(mensagem)


    print("\nPastelIA:", resposta)