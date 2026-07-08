from flask import Flask, request, jsonify, render_template

from nucleo.ia import responder

app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template("index.html")


@app.route("/mensagem", methods=["POST"])
def mensagem():

    dados = request.json

    texto = dados.get("mensagem", "")

    resposta = responder(texto)

    return jsonify(
        {
            "resposta": resposta
        }
    )


@app.route("/webhook", methods=["POST"])
def webhook():

    dados = request.json

    mensagem = dados.get(
        "mensagem",
        ""
    )

    resposta = responder(mensagem)

    return jsonify(
        {
            "resposta": resposta
        }
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )