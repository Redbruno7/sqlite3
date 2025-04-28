import sqlite3

conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\sqlite3_db2.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id_product INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL,
        image BLOB
    )
''')