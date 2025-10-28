import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(f"Base directory: {BASE_DIR}")

DB_PATH = BASE_DIR / "escola_v2.db"

if DB_PATH.exists():
    print(f"Banco encontrado em: {DB_PATH}")
else:
    print(f"Banco NÃO encontrado em: {DB_PATH}. Será criado ao conectar (se permissões permitirem).")

db_connection = sqlite3.connect(DB_PATH)
print(f"Conexão aberta com: {DB_PATH}")

cursor = db_connection.cursor()
cursor.execute("""
SELECT *
FROM Aluno
LIMIT 5;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)
    
db_connection.close()
print("Conexão fechada.")

