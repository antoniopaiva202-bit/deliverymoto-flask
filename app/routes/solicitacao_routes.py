from flask import Blueprint, render_template, request, redirect, session, flash
from app.services.sheets_service import abrir_planilha
import os
from datetime import datetime

solicitacao_bp = Blueprint("solicitacao", __name__)
SHEET_NAME = os.getenv("SHEET_NAME")

@solicitacao_bp.route("/solicitacao")
def solicitacao_page():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("solicitacao.html")

@solicitacao_bp.route("/solicitacao", methods=["POST"])
def solicitacao_post():
    if "usuario" not in session:
        return redirect("/login")

    planilha = abrir_planilha(SHEET_NAME)
    aba = planilha.worksheet("bd_py")

    data_hora_form = request.form["data_hora"]
    data_hora_formatada = datetime.fromisoformat(data_hora_form).strftime("%d/%m/%Y %H:%M")
    
    todas_linhas = aba.get_all_values()  
    if len(todas_linhas) > 1:
        
        try:
            ultimo_id = int(todas_linhas[-1][9])  
        except:
            ultimo_id = 0
    else:
        ultimo_id = 0

    proximo_id = str(ultimo_id + 1)
    status_inicial = "Pendente"

    dados = [
        request.form["solicitante"].upper(),
        request.form["endereco_retirada"].upper(),
        request.form["numero_retirada"].upper(),
        request.form["bairro_retirada"].upper(),
        request.form["cliente"].upper(),
        request.form["endereco_entrega"].upper(),
        request.form["numero_entrega"].upper(),
        request.form["bairro_entrega"].upper(),
        data_hora_formatada,
        proximo_id,
        status_inicial.upper()
    ]

    aba.append_row(dados)

    flash(f"Solicitação realizada com sucesso! Seu ID de solicitação é {proximo_id}.", "success")

    return redirect("/solicitacao")