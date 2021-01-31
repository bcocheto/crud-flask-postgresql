from application.model.client_model import Client
from application import app, db
from flask import render_template, redirect, url_for, request

# Rota responsável por editar clientes
@app.route("/edit/<int:codigo>", methods=["GET", "POST"])
def edit(codigo):

    cliente = Client.query.get(codigo)

    if request.method == "POST":
        cliente.nome = request.form["nome"]
        cliente.razao_social = request.form["razao_social"]
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("edit.html", cliente=cliente)