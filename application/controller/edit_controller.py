from application.model.client_model import Client
from application import app
from flask import render_template

# Rota para adicionar clientes
@app.route("/edit")
def edit():
    cliente = Client.query.all()
    return render_template("edit.html", cliente=cliente)