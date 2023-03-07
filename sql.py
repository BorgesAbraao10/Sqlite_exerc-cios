import sqlite3
conexao = sqlite3.connect('sql')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedor (id INT,nome VARCHAR(150) NOT NULL, endereco VARCHAR(150),produtos VARCHAR(20));')
cursor.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (1, 'Empresa de Leite ParmaLeite', 'Rua dos Leites, 23', 'leite');")

cursor.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 25', 'peixe');")
cursor.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Açougue Legal', 'Rua dos Leites, 30', 'carnes');")

cursor.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Açougue Novo', 'Rua dos Leites, 35', 'carnes');")

cursor.execute ('update fornecedor set endereco = "rua dos Peixes, 26" where id = 2')

visualizar = cursor.execute('select * from fornecedor')
for fornecedor in visualizar: 
    print (fornecedor)
   
cursor.execute ('delete from fornecedor where id = 1')


#cursor.execute('insert into fornecedor (id, nome, endereco, produtos) Values (3, "Padaria do Pão", "Penha", "Pão");')
#cursor.execute('insert into fornecedor (id, nome, endereco, produtos) Values (4, "Marcenaria Martelo", "Rua do Frei","Mesa");')
conexao.commit()
conexao.close