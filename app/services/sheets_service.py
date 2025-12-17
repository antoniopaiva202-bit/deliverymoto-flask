import gspread
import os
import json
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def abrir_planilha(nome):
    credenciais_json = os.getenv("GOOGLE_CREDENTIALS")

    if not credenciais_json:
        raise ValueError("Variável GOOGLE_CREDENTIALS não encontrada")

    credenciais_dict = json.loads(credenciais_json)

    credentials = Credentials.from_service_account_info(
        credenciais_dict,
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)
    return client.open(nome)
