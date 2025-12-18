from flask import Blueprint, render_template, request, redirect, flash
from app.services.sheets_service import abrir_planilha
import os

cadastro_bp = Blueprint("cadastro", __name__)
SHEET_NAME = os.getenv("SHEET_NAME")

@cadastro_bp.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@cadastro_bp.route("/cadastro", methods=["POST"])
def cadastro_post():
    nome = request.form["nome"].strip().upper()
    celular = request.form["celular"].strip()
    senha = request.form["senha"].strip()
    confirmar = request.form["confirmar_senha"].strip()

    if senha != confirmar:
        flash("As senhas não coincidem!", "erro")
        return redirect("/cadastro")

    planilha = abrir_planilha(SHEET_NAME)
    aba = planilha.worksheet("Dados_clientes")

    dados = aba.get_all_records()

    for linha in dados:
        if linha["Nome"] .upper() == nome:
            flash("Nome já cadastrado!", "erro")
            return redirect("/cadastro")

    aba.append_row([nome, celular, senha])

    flash("Cadastro realizado com sucesso, realize agora o login!", "sucesso")
    return redirect("/cadastro")
