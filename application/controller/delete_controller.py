from application.model.client_model import Client
from application import app
from flask import render_template


@app.route("/delete")
def delete():
    clientes = Client.query.all()
    return render_template("delete.html", clientes=clientes)