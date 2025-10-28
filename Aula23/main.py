# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# print(f"Base directory: {BASE_DIR}")

# DB_PATH = BASE_DIR / "escola_v2.db"

# if DB_PATH.exists():
#     print(f"Banco encontrado em: {DB_PATH}")
# else:
#     print(f"Banco NÃO encontrado em: {DB_PATH}. Será criado ao conectar (se permissões permitirem).")

# db_connection = sqlite3.connect(DB_PATH)
# print(f"Conexão aberta com: {DB_PATH}")

# cursor = db_connection.cursor()
# cursor.execute("""
# SELECT *
# FROM Aluno
# LIMIT 5;
# """)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
    
# db_connection.close()
# print("Conexão fechada.")

import sqlite3

# 1. Importar módulo e conectar ao banco de dados
conn = sqlite3.connect('escola_v2.db')
cursor = conn.cursor()

print("=" * 50)
print("1. CONEXÃO ESTABELECIDA COM SUCESSO")
print("=" * 50)

# 2. Query para pegar toda a tabela alunos e imprimir
print("\n2. TODOS OS ALUNOS:")
print("-" * 30)
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()

# Imprimir cabeçalho
cursor.execute("PRAGMA table_info(Aluno)")
colunas = [coluna[1] for coluna in cursor.fetchall()]
print(" | ".join(colunas))
print("-" * 80)

# Imprimir dados
for aluno in alunos:
    print(aluno)

# 3. Calcular média entre nota1 e nota2, ordenar e pegar os 10 maiores
print("\n3. TOP 10 ALUNOS COM MAIOR MÉDIA:")
print("-" * 40)
query_media = """
SELECT nome, nota1, nota2, 
ROUND((nota1 + nota2) / 2.0, 2) as media
FROM Aluno 
ORDER BY media DESC 
LIMIT 10
"""
cursor.execute(query_media)
top_alunos = cursor.fetchall()

# Imprimir resultados
print("NOME | NOTA1 | NOTA2 | MÉDIA")
print("-" * 50)
for aluno in top_alunos:
    print(f"{aluno[0]} | {aluno[1]} | {aluno[2]} | {aluno[3]}")

# 4. Left Join entre Aluno e Turma
print("\n4. LEFT JOIN - ALUNO E TURMA:")
print("-" * 35)
query_join = """
SELECT Aluno.*, Turma.* 
FROM Aluno 
LEFT JOIN Turma ON Aluno.id_turma = Turma.id
"""
cursor.execute(query_join)
resultados_join = cursor.fetchall()

# Obter nomes das colunas
cursor.execute("PRAGMA table_info(Aluno)")
colunas_aluno = [f"Aluno.{col[1]}" for col in cursor.fetchall()]

cursor.execute("PRAGMA table_info(Turma)")
colunas_turma = [f"Turma.{col[1]}" for col in cursor.fetchall()]

colunas_totais = colunas_aluno + colunas_turma
print(" | ".join(colunas_totais))
print("-" * 100)

for resultado in resultados_join:
    print(resultado)

# 5. Filtrar apenas alunos da turma 2
print("\n5. ALUNOS DA TURMA 2:")
print("-" * 25)
query_turma2 = """
SELECT Aluno.*, Turma.* 
FROM Aluno 
LEFT JOIN Turma ON Aluno.id_turma = Turma.id
WHERE Aluno.id_turma = 2
"""
cursor.execute(query_turma2)
alunos_turma2 = cursor.fetchall()

print(" | ".join(colunas_totais))
print("-" * 100)

for aluno in alunos_turma2:
    print(aluno)

# Fechar conexão
conn.close()
print("\n" + "=" * 50)
print("CONEXÃO FECHADA")
print("=" * 50)