import mysql.connector
# Se não apressentar erro ao executar o codigo o modulo foi instalado corretamente.

# Conectar ao banco de dados:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="finanças"
)


# Exibir banco de dados exitente:
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

mycursor = mydb.cursor()

# Criar tabela
# mycursor.execute("CREATE TABLE despesas (name VARCHAR(255), value int)")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
# resp = input("Bem vindo! \nInforme uma opção para prosseguir. \n1 - Visualizar despesas cadastradas \n2 - Visualzar saldo \n---> ")

print("BEM VINDO!!!")
mycursor.execute("SELECT name, value FROM renda")
myresult = mycursor.fetchall()

# para imprimir os valores sem parenteses é necessario anexar o resultado em uma lista
saldo = []
for x in myresult:
    print("O valor de " + x[0] )

# mycursor.execute("SELECT name, value FROM despesas")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#Caso selecione 2
# elif resp == "2":
#     print("teste")

# Caso não informe uma opção correta
# else:
#     print("Valor incorreto!")

# Inserir despesa no banco de dados
# name_desp = input("Informe o Nome da despesa: ")
# value_desp = input("Informe o Valor da despesa: ")
# sql = "INSERT INTO despesas (name, value) VALUES ('" +name_desp +"','" +value_desp +"')" 
# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "Valores inseridos!")
