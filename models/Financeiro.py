


class Financeiro:
    def __init__(self, periodo: str, receita: float, despesa: float):
        self.periodo = periodo
        self.receita = receita
        self.despesa = despesa
        self.saldo = receita - despesa
