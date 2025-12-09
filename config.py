import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

class Config:
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

    # Acesso ao Google Sheets
    GS_URL_SOLICITACAO = os.getenv("GS_URL_SOLICITACAO")
    GS_SECRET = os.getenv("GS_SECRET")
    GS_TIMEOUT = int(os.getenv("GS_TIMEOUT", 15))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    RETRY_DELAY = float(os.getenv("RETRY_DELAY", 0.5))
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")

    # Nome da planilha
    SHEET_NAME = os.getenv("SHEET_NAME", "STATUS DE ENTREGA PY")

    # Sal para senhas
    PASSWORD_SALT = os.getenv("PASSWORD_SALT", "salt_default")

