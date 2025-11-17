


class Exame:
    def __init__(self, paciente: str, profissional: str, tipo: str, resultado: str = None):
        self.paciente = paciente
        self.profissional = profissional
        self.tipo = tipo
        self.resultado = resultado
        self.concluido = bool(resultado)

    def registrar_resultado(self, resultado: str):
        self.resultado = resultado
        self.concluido = True
