


import datetime

class AuditService:
    def registrar(self, usuario, acao):
        agora = datetime.datetime.now().isoformat()
        log = f"[{agora}] Usuário {usuario} realizou ação: {acao}"
        print(log)  # por enquanto só imprime, depois podemos salvar em arquivo
