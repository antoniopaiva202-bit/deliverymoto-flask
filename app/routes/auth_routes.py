from flask import Blueprint, render_template, request, redirect, session, flash
from app.services.sheets_service import abrir_planilha
import os

auth_bp = Blueprint("auth", __name__)

SHEET_NAME = os.getenv("SHEET_NAME")

@auth_bp.route("/")
@auth_bp.route("/login")
def login():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login_post():
    nome = request.form["nome"]
    senha = request.form["senha"]

    planilha = abrir_planilha(SHEET_NAME)
    aba_clientes = planilha.worksheet("Dados_clientes")
    dados = aba_clientes.get_all_records()

    for linha in dados:
        if linha["Nome"] == nome and str(linha["Senha"]) == senha:
            session["usuario"] = nome
            return redirect("/solicitacao")

    flash("Usuário ou senha incorretos!", "erro")
    return redirect("/login")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
