


from models.Prontuario import Prontuario

class ProntuarioController:
    def registrar(self, paciente, descricao, profissional):
        return Prontuario(paciente, descricao, profissional)

    def listar(self, prontuarios):
        return prontuarios
