


# app/models/prescricao.py
class Prescricao:
    def __init__(self, id_: str, consulta_id: str, profissional_id: str, conteudo: str, assinatura_digital: str | None = None):
        self.id = id_
        self.consulta_id = consulta_id
        self.profissional_id = profissional_id
        self.conteudo = conteudo
        self.assinatura_digital = assinatura_digital

    def __str__(self):
        return f"Prescrição {self.id} - Consulta {self.consulta_id}"
