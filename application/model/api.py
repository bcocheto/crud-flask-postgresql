from application import db

# Classe responsável por gerenciar a estrutura do cliente


class Client(db.Model):
    __tablename__ = "cliente"
    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(64), unique=True)
    razao_social = db.Column(db.String(64), unique=True)
    cnpj = db.Column(db.String(64), unique=True)
    data_inclusao = db.Column(db.DateTime)

    def __init__(self, codigo, nome, razao_social, cnpj, data_inclusao):
        self.codigo = codigo
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = data_inclusao
