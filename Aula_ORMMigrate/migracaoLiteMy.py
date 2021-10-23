from databaseSqLite import dbLite, PetAdocao
from datetime import datetime

# --- Parte 1: Recebendo dados o SQLite que devem ser transferidos

print('---- Lista de Dados SALVOS SQLite ----')

pets_db = dbLite.session.query(PetAdocao).all()
for pet in pets_db:
    print(f'id: {pet.id}   Apelido: {pet.apelido}')

dbLite.session.close()

# --- Parte 2: Abrir o MySQL para salvar as novas informações

from databaseMySql import dbMy, PetAdocao

#--- Somente para fazer os testes o comando abaixo
dbMy.drop_all()
#------ Não esqueci de remover depois.. :)

dbMy.create_all()

print()
print('---- Adicionar os Dados MySQL ----')

for pet in pets_db:
    print(f'Adicionar:  {pet.apelido}')
    dbMy.session.add(PetAdocao(pet.apelido, pet.perfil, pet.dataregistro, pet.castrado, pet.responsavel, pet.contato))

dbMy.session.add(PetAdocao('leao', 'calmo', datetime.strptime('2021-10-23', '%Y-%m-%d'), False, 'Nisflei', 'nn@gmail.com'))
dbMy.session.commit()
