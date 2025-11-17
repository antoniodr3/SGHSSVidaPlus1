


from flask import Flask, render_template, request
# Importar modelos
from models.Paciente import Paciente
from models.Profissional import Profissional
from models.Consulta import Consulta
from models.Prontuario import Prontuario
from models.Prescricao import Prescricao
from models.Exame import Exame
from models.Leito import Leito
from models.Financeiro import Financeiro
from models.Teleconsulta import Teleconsulta
from models.Usuario import Usuario

app = Flask(__name__)

# ------------------ HOME ------------------
@app.route("/")
def home():
    return render_template("home.html")


# ------------------ PACIENTE ------------------
@app.route("/paciente/cadastro", methods=["GET", "POST"])
def paciente_cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = int(request.form.get("idade"))
        documento = request.form.get("documento")
        paciente = Paciente(nome, idade, documento)
        return f"Paciente {paciente.nome} cadastrado com sucesso!"
    return render_template("paciente/cadastro.html")

# ------------------ PROFISSIONAL ------------------
@app.route("/profissional/cadastro", methods=["GET", "POST"])
def profissional_cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        especialidade = request.form.get("especialidade")
        registro = request.form.get("registro")
        profissional = Profissional(nome, especialidade, registro)
        return f"Profissional {profissional.nome} ({profissional.especialidade}) cadastrado com sucesso!"
    return render_template("profissional/cadastro.html")

# ------------------ CONSULTA ------------------
@app.route("/consulta/agendar", methods=["GET", "POST"])
def consulta_agendar():
    if request.method == "POST":
        paciente = request.form.get("paciente")
        profissional = request.form.get("profissional")
        horario = request.form.get("horario")
        consulta = Consulta(paciente, profissional, horario)
        return f"Consulta agendada para {consulta.paciente} com {consulta.profissional} em {consulta.horario}"
    return render_template("consulta/agendar.html")

# ------------------ PRONTUÁRIO ------------------
@app.route("/prontuario/cadastro", methods=["GET", "POST"])
def prontuario_cadastro():
    if request.method == "POST":
        paciente = request.form.get("paciente")
        descricao = request.form.get("descricao")
        profissional = request.form.get("profissional")
        prontuario = Prontuario(paciente, descricao, profissional)
        return f"Prontuário do paciente {prontuario.paciente} registrado por {prontuario.profissional}"
    return render_template("prontuario/cadastro.html")

# ------------------ PRESCRIÇÃO ------------------
@app.route("/prescricao/cadastro", methods=["GET", "POST"])
def prescricao_cadastro():
    if request.method == "POST":
        paciente = request.form.get("paciente")
        profissional = request.form.get("profissional")
        medicamento = request.form.get("medicamento")
        dosagem = request.form.get("dosagem")
        instrucoes = request.form.get("instrucoes")
        prescricao = Prescricao(paciente, profissional, medicamento, dosagem, instrucoes)
        return f"Prescrição emitida para {prescricao.paciente}: {prescricao.medicamento} - {prescricao.dosagem}"
    return render_template("prescricao/cadastro.html")

# ------------------ EXAME ------------------
@app.route("/exame/cadastro", methods=["GET", "POST"])
def exame_cadastro():
    if request.method == "POST":
        paciente = request.form.get("paciente")
        profissional = request.form.get("profissional")
        tipo = request.form.get("tipo")
        resultado = request.form.get("resultado")
        exame = Exame(paciente, profissional, tipo, resultado)
        return f"Exame {exame.tipo} para {exame.paciente} registrado. Resultado: {exame.resultado or 'pendente'}"
    return render_template("exame/cadastro.html")

# ------------------ ADMINISTRAÇÃO: LEITOS ------------------
@app.route("/admin/leitos", methods=["GET", "POST"])
def admin_leitos():
    if request.method == "POST":
        numero = request.form.get("numero")
        status = request.form.get("status")
        leito = Leito(numero, status)
        return f"Leito {leito.numero} registrado com status {leito.status}"
    return render_template("admin/leitos.html")

# ------------------ ADMINISTRAÇÃO: RELATÓRIOS ------------------
@app.route("/admin/relatorios", methods=["GET", "POST"])
def admin_relatorios():
    if request.method == "POST":
        periodo = request.form.get("periodo")
        receita = request.form.get("receita")
        despesa = request.form.get("despesa")
        relatorio = Financeiro(periodo, float(receita), float(despesa))
        return f"Relatório {relatorio.periodo}: Receita {relatorio.receita}, Despesa {relatorio.despesa}, Saldo {relatorio.saldo}"
    return render_template("admin/relatorios.html")

# ------------------ TELEMEDICINA ------------------
@app.route("/telemedicina/sala", methods=["GET", "POST"])
def telemedicina_sala():
    if request.method == "POST":
        paciente = request.form.get("paciente")
        profissional = request.form.get("profissional")
        descricao = request.form.get("descricao")
        teleconsulta = Teleconsulta(paciente, profissional, descricao)
        teleconsulta.iniciar()
        return f"Teleconsulta iniciada entre {teleconsulta.paciente} e {teleconsulta.profissional}. Status: {teleconsulta.status}"
    return render_template("telemedicina/sala.html")

# ------------------ SEGURANÇA ------------------
@app.route("/seguranca/login", methods=["GET", "POST"])
def seguranca_login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        perfil = request.form.get("perfil")
        user = Usuario(usuario, senha, perfil)
        return f"Login realizado com sucesso! Perfil: {user.perfil}"
    return render_template("seguranca/login.html")

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)

