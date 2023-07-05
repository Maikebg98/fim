import mysql.connector
# Se não apressentar erro ao executar o codigo o modulo foi instalado corretamente.

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

print(mydb)