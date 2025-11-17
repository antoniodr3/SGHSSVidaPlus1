


# app/models/prontuario.py
class Prontuario:
    def __init__(self, paciente: str, descricao: str, profissional: str):
        self.paciente = paciente
        self.descricao = descricao
        self.profissional = profissional
        self.data = None
