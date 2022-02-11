import os

import dotenv
import sqlalchemy


def connect_db_postgres(dotenv_path=os.path.expanduser("~/.env")):
    """Função para se conectar no banco de dados

    Args:
        dotenv_path (caminho das variaveis de ambiente, optional):
        pesquisa .env iniciando na raiz do usuario caso ele não passe um caminho.
        caminho padrão: os.path.expanduser("~/.env").

    Returns:
        conexao: retorna a conexao com o banco de dados postgres
    """
