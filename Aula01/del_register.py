import os
import sqlite3

conn = sqlite3.connect('C:\Bruno - Técnico DS\sqlite3\meu_banco_de_dados.db')

cursor = conn.cursor()

os.system('cls')

client_name = input('Enter client name do delete: ')

# Execute delete based on the name provided by user
cursor.execute('DELETE FROM clients WHERE client_name = ?', (client_name,))
conn.commit()

print('Client deleted successfully!')
print()

# Close connection
conn.close()