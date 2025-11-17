


# app/models/hospital.py
class Hospital:
    def __init__(self, id_: str, nome: str, total_leitos: int):
        self.id = id_
        self.nome = nome
        self.total_leitos = total_leitos
        self.leitos_ocupados = 0
        self.suprimentos: dict[str, int] = {}

    def ocupar_leito(self) -> bool:
        if self.leitos_ocupados < self.total_leitos:
            self.leitos_ocupados += 1
            return True
        return False

    def liberar_leito(self) -> bool:
        if self.leitos_ocupados > 0:
            self.leitos_ocupados -= 1
            return True
        return False

    def adicionar_suprimento(self, nome: str, quantidade: int):
        self.suprimentos[nome] = self.suprimentos.get(nome, 0) + quantidade

    def __str__(self):
        return f"Hospital {self.nome} - Leitos {self.leitos_ocupados}/{self.total_leitos}"
