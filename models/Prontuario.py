


# app/models/prontuario.py
class Prontuario:
    def __init__(self, id_: str, paciente_id: str, profissional_id: str, data_iso: str, notas: str):
        self.id = id_
        self.paciente_id = paciente_id
        self.profissional_id = profissional_id
        self.data_iso = data_iso
        self.notas = notas

    def __str__(self):
        return f"Prontuário {self.id} - Paciente {self.paciente_id}"
