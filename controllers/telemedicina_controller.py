


from models.Teleconsulta import Teleconsulta

class TelemedicinaController:
    def agendar(self, paciente, profissional, descricao):
        return Teleconsulta(paciente, profissional, descricao)

    def iniciar(self, teleconsulta: Teleconsulta):
        teleconsulta.iniciar()
        return teleconsulta

    def finalizar(self, teleconsulta: Teleconsulta):
        teleconsulta.finalizar()
        return teleconsulta
