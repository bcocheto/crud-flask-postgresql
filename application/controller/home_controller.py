from application import app
from flask import render_template, current_app


@app.route("/")
@app.route("/home")
def index():

    return render_template("list.html")
