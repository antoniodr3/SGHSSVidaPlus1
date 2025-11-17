


from models.Exame import Exame

class ExameController:
    def solicitar(self, paciente, profissional, tipo):
        return Exame(paciente, profissional, tipo)

    def concluir(self, exame: Exame, resultado: str):
        exame.registrar_resultado(resultado)
        return exame
