# Preparando as dependencias
#python - m pip install --upgrade pip
# flask: microframework para criação de aplicativos web
# sqlalchemy: ORM para trabalhar com banco de dados
# flask-sqlalchemy: integração entre flask e sqlalchemy
# pymysql: driver de conexão com o banco de dados MySQL

from databaseModel import db, Pet_adocao
from datetime import datetime

#limpando somente para teste
#db.drop_all()
#db.create_all()

pets = [
     Pet_adocao('Furação','Docil',datetime.strptime('2021-09-26', '%Y-%m-%d'),True,'Ana Maria Braga','ana@gmail.com'),
    Pet_adocao('fofinho', 'bravo', datetime.strptime('2021-09-26', '%Y-%m-%d'), True, 'Fausto Silva', 'fausto@gmail.com'),
    Pet_adocao('maiau', 'docil', datetime.strptime('2021-09-26', '%Y-%m-%d'), False, 'Pedro Bial','pedro@gmail.com'),
    Pet_adocao('costelinha', 'bravo', datetime.strptime('2021-09-26', '%Y-%m-%d'), False, 'Jose J', 'jj@gmail.com')
]
print(pets)

toto = Pet_adocao('Toto','nervoso, mas é brincalhao',datetime.strptime('2021-09-25','%Y-%m-%d'),False,'Nisflei','nisflei@gmail.com')
print(toto.apelido)
db.session.add(toto)
db.session.commit()

print()
print('>--- Adicionar a Lista no Banco de Dados')
for pet in pets:
    print(f'Salvando: {pet.apelido}-{pet.responsavel}')
    db.session.add(pet)
db.session.commit()

#Consultando informações no BD
print()
print('>--- Lendo os dados do Banco')
pets_bd = db.session.query(Pet_adocao).all()

for pet in pets_bd:
    print(f'id:{pet.id} - {pet.apelido} - {pet.perfil} - {pet.contato} : {pet.responsavel}')


# Consultar apenas 1 registro no Banco de Dados
pet_temp = Pet_adocao.query.filter_by(id=13).first()
print(f'{pet_temp.id} - {pet_temp.apelido}')

# Removendo esse registro
db.session.delete(pet_temp)
db.session.commit()
