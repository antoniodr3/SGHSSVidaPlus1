


from models.Leito import Leito

class LeitoController:
    def registrar(self, numero, status="livre"):
        return Leito(numero, status)

    def atualizar_status(self, leito: Leito, status: str):
        leito.status = status
        return leito
