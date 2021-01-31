from application.model.client_model import Client
from application import app, db
from flask import redirect, url_for

# Rota responsável por deletar clientes
@app.route("/delete/<int:codigo>")
def delete(codigo):
    cliente = Client.query.get(codigo)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for("index"))
