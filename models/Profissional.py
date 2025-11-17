


# app/models/profissional.py
from typing import List

class Profissional:
    def __init__(self, id_: str, nome: str, registro: str, especialidade: str, cargo: str):
        self.id = id_
        self.nome = nome
        self.registro = registro
        self.especialidade = especialidade
        self.cargo = cargo
        self.agenda: List[str] = []

    def __str__(self):
        return f"{self.cargo} {self.nome} - {self.especialidade}"


