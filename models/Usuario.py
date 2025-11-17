


class Usuario:
    def __init__(self, usuario: str, senha: str, perfil: str):
        self.usuario = usuario
        self.senha = senha  # em produção: armazenar criptografada
        self.perfil = perfil
