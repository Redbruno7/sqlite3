import os
import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\meu_banco_de_dados.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM clients")
results = cursor.fetchall()

os.system('cls')

# Create table with PrettyTable and set column names
table = PrettyTable()

# Get column names by cursor.description
columns = [description[0] for description in cursor.description]

# Set column names in table
table.field_names = columns

# Add rows to table
for row in results:
    table.add_row(row)

print(table)
print()
conn.close()