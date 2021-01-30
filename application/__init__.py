from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/templates"),
)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:root@127.0.0.1:5432/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from application.model.api import Client

db.create_all()
db.session.commit()

from application.controller import home_controller
