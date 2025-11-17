


# app/models/consulta.py
class Consulta:
    def __init__(self, paciente: str, profissional: str, horario: str):
        self.paciente = paciente
        self.profissional = profissional
        self.horario = horario
        self.realizada = False

    def realizar(self):
        self.realizada = True
