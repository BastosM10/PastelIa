import requests


resposta = requests.post(
    "http://127.0.0.1:5000/mensagem",
    json={
        "mensagem": "João 3 anotado"
    }
)


print(resposta.text)