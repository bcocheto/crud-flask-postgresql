from application import app
from flask import render_template


@app.route("/add")
def add():
    return render_template("add.html")