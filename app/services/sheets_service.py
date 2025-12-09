import gspread
from google.oauth2.service_account import Credentials
import os

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def abrir_planilha(nome):
    caminho_credenciais = os.getenv("GOOGLE_CREDENTIALS_JSON")

    if not caminho_credenciais:
        raise ValueError("Variável GOOGLE_CREDENTIALS_JSON não encontrada!")

    if not os.path.exists(caminho_credenciais):
        raise FileNotFoundError(f"Arquivo de credenciais não encontrado: {caminho_credenciais}")

    credentials = Credentials.from_service_account_file(
        caminho_credenciais,
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)
    return client.open(nome)
