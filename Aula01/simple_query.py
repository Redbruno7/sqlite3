import os
import sqlite3

conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\meu_banco_de_dados.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clients")
results = cursor.fetchall()

os.system('cls')
for row in results:
    print(row)
print()
conn.close()