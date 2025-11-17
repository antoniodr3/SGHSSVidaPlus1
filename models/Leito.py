


class Leito:
    def __init__(self, numero: str, status: str = "livre"):
        self.numero = numero
        self.status = status

    def ocupar(self):
        self.status = "ocupado"

    def liberar(self):
        self.status = "livre"

    def manutencao(self):
        self.status = "manutencao"
