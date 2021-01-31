from application import db
import datetime

# Classe responsável por gerenciar a estrutura do cliente


class Client(db.Model):
    __tablename__ = "cliente"
    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(64), unique=True)
    razao_social = db.Column(db.String(64), unique=True)
    cnpj = db.Column(db.String(64), unique=True)
    data_inclusao = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, nome, razao_social, cnpj):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
