import mysql.connector

con = mysql.connector.connect(host='localhost',database='MeuDB',user='root',password='Info@1234')

if con.is_connected():
    # ver informações do servidor MySQL
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)

    #enviar um comando SQL para o Servidor MySQL
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")

