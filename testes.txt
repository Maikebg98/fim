import mysql.connector

# Conectar ao banco de dados:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="finanças"
)

resp = ""
# Menu
while resp == "":
    resp = input("\nSelecione uma opção para contnuar: \n1 - Visualizar despesas \n2 -  Cadastrar nova despesa \n---> ")
    
    if resp == "1":
        print("\n")
        print("Buscando informações...")

        mycursor = mydb.cursor()
        sql = "SELECT name, value FROM despesas"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        nome_despesa = []
        for x in myresult:
            nome_despesa.append(x[0])
            print(x[0])
        print(nome_despesa)

        # nome_despesa = []
        # for x in myresult:
        #     print(x[0])
        #     nome_despesa.append(x[0])
        #     resp = ""
        
        # mycursor = mydb.cursor()
        # mycursor.execute("SELECT value FROM despesas")
        # myresult = mycursor.fetchall()
        # value_despesa = []
        # for x in myresult:
        #     print(x[0])
        #     value_despesa.append()
        
    elif resp == "2":
        # Inserir despesa no banco de dados
        mycursor = mydb.cursor()
        name_desp = input("Informe o Nome da despesa: ")
        value_desp = input("Informe o Valor da despesa: ")
        mycursor.execute("INSERT INTO despesas (name, value) VALUES ('" +name_desp +"','" +value_desp +"')" )
        mydb.commit()
        print("\nDespesa cadastrada com sucesso!\n")
        resp = ""
        pass

    else:
        print("\nOPÇÃO INVALIDA! \n")
        resp = ""
        pass