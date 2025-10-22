# treinando sqlite com python
import sqlite3
# criando uma conexao
conexao = sqlite3.connect('aula21.db')
# criando um cursor
cursor = conexao.cursor()
# criando uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')
# inserindo dados
cursor.execute('''
INSERT INTO alunos (nome, idade) VALUES
('João', 20),
('Maria', 22),
('Pedro', 21)
''')
# salvando as alterações
conexao.commit()
# consultando dados
cursor.execute('SELECT * FROM alunos')
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)
# fechando a conexao
# conexao.close()

# outros exemmplos de sql com python
# atualizando dados
cursor.execute('''
UPDATE alunos SET idade = 22 WHERE id = 2
''')
# excluindo dados
cursor.execute('''
DELETE FROM alunos WHERE id = 3
''')
# salvando as alterações
conexao.commit()
# consultando dados novamente
cursor.execute('SELECT * FROM alunos')
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)
# fechando a conexao
conexao.close()