# Com esta base de dados, vamos criar a aplicação CLI TODO com as funcionalidades:

# Criar, atualizar e excluir um TODO;

# Criar, atualizar e excluir categorias;

# Listar todos os afazeres de um dia específico;

# Listar todas as categorias;

# Marcar uma tarefa como concluída.

import sqlite3 
conexao = sqlite3.connect('banco_tarefas')
cursor = conexao.cursor()

cursor.execute('Create table if not exists categoria(id integer not null primary key autoincrement,nome varchar(100))')
cursor.execute('Create table if not exists tarefas(id integer not null primary key autoincrement,nome varchar(100), id_categoria int not null, foreign key (id_categoria)references categoria(id))')
cursor.execute('alter table tarefas add column conclusao int')
cursor.execute('Insert into categoria (nome) values ("Estudar")')
cursor.execute('Insert into tarefas (nome, id_categoria,conclusao) values ("Estudar",2,0)')
cursor.execute('update tarefas set conclusao = 1 where id = 2')
cursor.execute('update tarefas set data = "20230306" where id = 1')
cursor.execute('update tarefas set data = "20230307" where id = 2')
cursor.execute('alter table tarefas add column data varchar (12)')
categorias = cursor.execute('select * from tarefas where data = "20230306" ')
for categoria in categorias : 
    print (categoria)
cursor.execute('delete from tarefas where id = 2')



conexao.commit()
conexao.close
