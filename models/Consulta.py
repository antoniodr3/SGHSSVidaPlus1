


# app/models/consulta.py
class Consulta:
    def __init__(self, id_: str, paciente_id: str, profissional_id: str, data_iso: str, status: str = "agendada"):
        self.id = id_
        self.paciente_id = paciente_id
        self.profissional_id = profissional_id
        self.data_iso = data_iso
        self.status = status
        self.telemedicina = False

    def __str__(self):
        return f"Consulta {self.id} em {self.data_iso} - Status: {self.status}"
