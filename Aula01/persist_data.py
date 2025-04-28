import sqlite3

# Connection with database
conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\meu_banco_de_dados.db")

cursor = conn.cursor()

# Set data tuple
client_data = ('João Silva', 30)

# Placeholders (?, ?): used as placeholders.
# They will be replaced by the tuple values "client_data"
# It is recommended to use placeholders because it protects against SQL injection attacks
cursor.execute('INSERT INTO clients (client_name, age) VALUES (?, ?)', client_data)

many_clients_data = [
    ('Maria Souza', 25),
    ('Carlos Pereira', 35),
    ('Pedro José', 28),
    ('Ana Costa', 28),
    ('Luís Gomes', 30),
    ('Fernanda Lima', 22),
    ('Roberto Silva', 40),
    ('Juliana Almeida', 33),
    ('Lucas Martins', 27),
    ('Sofia Ferreira', 31),
]

cursor.executemany(
    "INSERT INTO clients(client_name, age) VALUES (?, ?)", many_clients_data
)

# Save transaction in database
conn.commit()

# Close connection
conn.close()