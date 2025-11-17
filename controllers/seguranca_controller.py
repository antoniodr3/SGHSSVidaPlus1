


from models.Usuario import Usuario

class SegurancaController:
    def autenticar(self, usuario, senha, perfil):
        # Aqui seria feita a validação real (ex: banco de dados + hash da senha)
        if usuario and senha and perfil:
            return Usuario(usuario, senha, perfil)
        return None

    def verificar_perfil(self, usuario: Usuario, perfil_necessario: str):
        return usuario.perfil == perfil_necessario
