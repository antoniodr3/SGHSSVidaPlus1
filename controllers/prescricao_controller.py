


from models.Prescricao import Prescricao

class PrescricaoController:
    def emitir(self, paciente, profissional, medicamento, dosagem, instrucoes):
        return Prescricao(paciente, profissional, medicamento, dosagem, instrucoes)
