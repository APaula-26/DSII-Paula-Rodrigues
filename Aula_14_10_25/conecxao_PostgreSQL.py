# pip install psycopg2
import psycopg2
conexao = psycopg2.connect(host="127.0.0.1", database="senai", user="postgres", password="senai", port=5432)
cursor = conexao.cursor()
cons = "INSERT INTO clientes(cliente, estado, sexo, status) VALUES('Silvio Santos', 'RJ', 'M', 'Diamond')"
cursor.execute(cons)
conexao.commit() #Comando que salva as informações salvas anteriormente 
consulta = "SELECT * FROM clientes" #Realiza uma consulta na tabela de clientes 
cursor.execute(consulta)
registros = cursor.fetchall() # A partir daqui ele vai pegar as informações na ordem dada e ir imprimindo os valores 
for row in registros:
    print("Nome = ", row[1])
    print("Estado = ", row[2])
    print("Status  = ", row[4], "\n")
cursor.close()
conexao.close() #Fecha a conecxao do banco de dados para não ter vazamento de dados. 