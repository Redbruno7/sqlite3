import os
import sqlite3

conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\meu_banco_de_dados.db")

cursor = conn.cursor()

os.system('cls')
client_name = input('Enter client name: ')
new_age = int(input('Enter new age: '))

# Update age based on name provide by user
cursor.execute('UPDATE clients SET age = ? WHERE client_name = ?',
    (new_age, client_name))

# Save changes in database
conn.commit()
print("Data Update Successfully!")
print()
conn.close()