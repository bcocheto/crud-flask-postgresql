from application import app
from flask import render_template
from application.model.client_model import Client


@app.route("/")
@app.route("/home")
def index():
    clientes = Client.query.all()
    return render_template("list.html", clientes=clientes)
