


from models.Financeiro import Financeiro

class FinanceiroController:
    def gerar_relatorio(self, periodo, receita, despesa):
        return Financeiro(periodo, float(receita), float(despesa))
