


# app/models/paciente.py
from typing import List

class Paciente:
    def __init__(self, id_: str, nome: str, cpf: str, idade: int, contato: str, email: str):
        self.id = id_
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.contato = contato
        self.email = email
        self.consultas: List[str] = []
        self.prontuarios: List[str] = []
        self.notificacoes: List[str] = []

    def __str__(self):
        return f"Paciente {self.nome} (CPF: {self.cpf})"
