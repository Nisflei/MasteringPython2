#Python - Preparação de Ambiente 

- Utilizar a ferramenta Pycharm
 
link: https://www.jetbrains.com/pt-br/pycharm/download/

* Lembre-se de usar a verão Community


# Usar o New Projet no Pycharm para indicar o VIRTUAL ENV

- Pacotes são carregados na pasta ENV (Ambiente Virtual)


- Para instalar pacotes externos (Bibliotecas) 
- Voce precisa usar: pip install <biblioteca> ex:
- Abrir o Terminal no PyCharm

pip install pandas
pip install openpyxl

 
# Instalar o Mysql

link: mysql.com
- Abrir Downloads: MySQL Community (GPL) Downloads »
- Selecionar a versão correpondente ao sistema operacional (neste caso MySQL Installer for Windows)

* Lembre-se:
    - Voce pode custormizar a instalação ou colocar a padrão.
    - Escolher a opção DEVELOPMENT quando solicitado 
    - O usuario padrão é root, e voce no momento da instalação deve definir uma senha

- Agora instale o MySQLWorkbench (software amigavel para Administrar o MySQL  


# Conectar o Pyton no MySQL 

- pip install mysql-connector-python

# Podemos gerar uma lista de REQUERIMENTOS instalados no Ambiente Virtual 

Abrir o Terminal do Pycharm

- pip install pip-chill

Para criar a lista de dependencias para o projeto
- pip freeze > requirements.txt
- pip-chill  > requirements.txt


Para recarregar automaticamente quando abrir o projeto em outro ambiente:
- pip install -r requirements.txt 




