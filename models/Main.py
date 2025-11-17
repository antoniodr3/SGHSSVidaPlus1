


# main.py
from models.Paciente import Paciente
from models.Profissional import Profissional
from models.Consulta import Consulta

def main():
    print("Sistema VidaPlus iniciado!")
    # Exemplo de uso
    paciente = Paciente(nome="João", idade=30)
    profissional = Profissional(nome="Dra. Ana", especialidade="Cardiologia")
    consulta = Consulta(paciente=paciente, profissional=profissional)
    consulta.realizar()

if __name__ == "__main__":
    main()
