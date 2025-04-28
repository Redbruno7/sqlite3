import sqlite3

# Conection with database
conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\meu_banco_de_dados.db")

# For database operations, will be required a cursor, which is an object that execute SQL commands
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT NOT NULL,
        age INTEGER
    )
''')