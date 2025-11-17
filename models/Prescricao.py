


# app/models/prescricao.py
class Prescricao:
    def __init__(self, paciente: str, profissional: str, medicamento: str, dosagem: str, instrucoes: str):
        self.paciente = paciente
        self.profissional = profissional
        self.medicamento = medicamento
        self.dosagem = dosagem
        self.instrucoes = instrucoes
        self.emitida = True
