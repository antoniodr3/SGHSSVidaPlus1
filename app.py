


from flask import Flask, render_template, request
from models.Paciente import Paciente  # opcional, se quiser instanciar a classe

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bem-vindo ao Sistema VidaPlus</h1><a href='/paciente/cadastro'>Cadastrar paciente</a>"

@app.route("/paciente/cadastro", methods=["GET", "POST"])
def paciente_cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = int(request.form.get("idade"))
        documento = request.form.get("documento")
        # opcional: instanciar a classe Paciente
        p = Paciente(nome=nome, idade=idade, documento=documento)
        return f"Paciente {p.nome} cadastrado com sucesso!"
    return render_template("paciente/cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)
