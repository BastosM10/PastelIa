class Contexto:

    def __init__(self):
        self.ultima_mensagem = None
        self.assunto = None


    def atualizar(self, mensagem):
        self.ultima_mensagem = mensagem


    def obter(self):
        return self.ultima_mensagem