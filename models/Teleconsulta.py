


class Teleconsulta:
    def __init__(self, paciente: str, profissional: str, descricao: str):
        self.paciente = paciente
        self.profissional = profissional
        self.descricao = descricao
        self.status = "agendada"

    def iniciar(self):
        self.status = "em andamento"

    def finalizar(self):
        self.status = "concluída"
