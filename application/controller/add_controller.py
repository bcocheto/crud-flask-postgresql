from application.model.client_model import Client
from flask.helpers import url_for
from werkzeug.utils import redirect
from application import db
from application import app
from flask import render_template, request

# Rota para adicionar clientes
@app.route("/add", methods=["GET", "POST"])
def add():
    clientes = Client.query.all()
    if request.method == "POST":
        clientes = Client(
            request.form["nome"],
            request.form["razao_social"],
            request.form["cnpj"],
        )
        db.session.add(clientes)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")