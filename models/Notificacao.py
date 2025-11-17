


# app/models/notificacao.py
class Notificacao:
    def __init__(self, id_: str, paciente_id: str, titulo: str, mensagem: str, lida: bool = False):
        self.id = id_
        self.paciente_id = paciente_id
        self.titulo = titulo
        self.mensagem = mensagem
        self.lida = lida

    def __str__(self):
        return f"Notificação {self.id} - {self.titulo}"
