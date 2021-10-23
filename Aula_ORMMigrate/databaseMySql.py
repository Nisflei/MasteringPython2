from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userbd:Teste#1234@localhost:3306/MeuDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbMy = SQLAlchemy(app)

class PetAdocao(dbMy.Model):
    id = dbMy.Column(dbMy.Integer, primary_key=True )
    apelido = dbMy.Column(dbMy.String(500), unique=True )
    perfil = dbMy.Column(dbMy.String(200))
    dataregistro = dbMy.Column(dbMy.DateTime())
    castrado = dbMy.Column(dbMy.Boolean, default=True)
    responsavel = dbMy.Column(dbMy.String(200), nullable=True)
    contato = dbMy.Column(dbMy.String(100), nullable=True)

    def __init__(self, apelido, perfil, dataregistro, castrado, responsavel, contato ):
        self.apelido = apelido
        self.perfil = perfil
        self.dataregistro = dataregistro
        self.castrado = castrado
        self.responsavel = responsavel
        self. contato = contato

