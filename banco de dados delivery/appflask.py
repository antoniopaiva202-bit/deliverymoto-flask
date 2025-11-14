from flask import Flask, render_template, request, redirect
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)


SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
CREDENCIAIS = Credentials.from_service_account_file(
    r"C:\Users\User\Documents\PROJETOS PYTHON\banco de dados delivery\service_account_cred.json",
    scopes=SCOPES
)
CLIENT = gspread.authorize(CREDENCIAIS)

SHEET_NAME = "STATUS DE ENTREGA PY"
TAB_NAME = "bd_py"

@app.route("/solicitacao")
def home():
    return render_template("solicitacao.html")

@app.route("/solicitacao", methods=["POST"])
def solicitacao():
    solicitante = request.form["solicitante"]
    endereco_retirada = request.form["endereco_retirada"]
    numero_retirada = request.form["numero_retirada"]
    bairro_retirada = request.form["bairro_retirada"]
    cliente = request.form["cliente"]
    endereco_entrega = request.form["endereco_entrega"]
    numero_entrega = request.form["numero_entrega"]
    bairro_entrega = request.form["bairro_entrega"]
    data_hora = request.form["data_hora"]


    planilha = CLIENT.open(SHEET_NAME)
    aba = planilha.worksheet(TAB_NAME)

  
    aba.append_row([
        solicitante, endereco_retirada, numero_retirada, bairro_retirada,
        cliente, endereco_entrega, numero_entrega, bairro_entrega, data_hora
    ])

    return redirect("/solicitacao")

if __name__ == "__main__":
    app.run(debug=True)
