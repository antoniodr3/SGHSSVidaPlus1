


from models.Consulta import Consulta

class ConsultaController:
    def agendar(self, paciente, profissional, horario):
        return Consulta(paciente, profissional, horario)

    def realizar(self, consulta: Consulta):
        consulta.realizar()
        return consulta
