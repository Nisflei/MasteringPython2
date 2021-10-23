from databaseSqLite import dbLite, PetAdocao
#from databaseMySql import dbLite, PetAdocao
from datetime import datetime

#--- Somente para fazer os testes o comando abaixo
dbLite.drop_all()
dbLite.create_all()
#------ Não esqueci de remover depois.. :)


pets = [
    PetAdocao('furação','docil',datetime.strptime('2021-09-26', '%Y-%m-%d'),True,'Ana Maria Braga','ana@gmail.com'),
    PetAdocao('fofinho', 'bravo', datetime.strptime('2021-09-26', '%Y-%m-%d'), True, 'Fausto Silva', 'fausto@gmail.com'),
    PetAdocao('maiau', 'docil', datetime.strptime('2021-09-26', '%Y-%m-%d'), False, 'Pedro Bial','pedro@gmail.com'),
    PetAdocao('costelinha', 'bravo', datetime.strptime('2021-10-23', '%Y-%m-%d'), False, 'Jose J', 'jj@gmail.com')
]

for pet in pets:
    print(f'Adicionar:  {pet.apelido}')
    dbLite.session.add(pet)

dbLite.session.commit()

# -- Parte 2: Lendo os dados gravados

print()
print('---- Lista de Dados SALVOS ----')

pets_db = dbLite.session.query(PetAdocao).all()
for pet in pets_db:
    print(f'id: {pet.id}   Apelido: {pet.apelido}')

dbLite.session.close()
