# Library to work with databases SQLite3
import sqlite3

# Library to show formated tables
from prettytable import PrettyTable

# Import pathlib module to work with relative paths or absolut paths
from pathlib import Path
import os

os.system('cls')

# Conection with database (file will be create if not exist)

# Relative path
conn = sqlite3.connect("C:\Bruno - Técnico DS\sqlite3\db_rel_1_n.db")
cursor = conn.cursor()

# Create "Clients" table (Main Table)
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    city TEXT
)
''')

# Create "Requests" table (Related table)
cursor.execute('''
CREATE TABLE IF NOT EXISTS requests (
    id_request INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    date TEXT NOT NULL,
    total_value REAL NOT NULL,
    FOREIGN KEY (id_client) REFERENCES Clients (id_client)
)
''')


# Function to verify if a client exists in database
def client_exists(id_client):
    cursor.execute(
        'SELECT 1 FROM clients WHERE id_client = ?', (id_client,)
    )

    # Return True if client exists, false if not
    return cursor.fetchone() is not None


# Function to insert data in "Clients" table
def insert_client():
    client_name = input('Enter client name: ')
    email = input('Enter email client: ')
    phone = input('Enter phone client: ')
    city = input('Enter city client: ')
    cursor.execute('''
    INSERT INTO clients (client_name, email, phone, city)
    VALUES (?, ?, ?, ?)
    ''', (client_name, email, phone, city))
    conn.commit()
    print('Client inserted successfully!')


# Function to insert data in "Requests" table
def insert_request():

    # List clients
    cursor.execute('''
    SELECT * from clients
    ''')
    results = cursor.fetchall()

    # Don't make request without clients
    if not results:
        print('-' * 80)
        print('No client found. Register client first.')
        print('-' * 80)
        return
    
    # Create and format table to show
    table = PrettyTable(['id_client', 'Name', 'Email', 'Phone', 'City'])
    for row in results:
        table.add_row(row)
    print(table)

    try:

        # Ensure ID be a integer number
        id_client = int(input('Enter client ID: '))

        # Verify client exists
        if not client_exists(id_client):
            print('-' * 80)
            print(f'Error: Client ID {id_client} not founded.')
            print('Register client first.')
            print('-' * 80)

            # Return to menu if client doesn't exists
            return
        
        # Request order data
        product_name = input('Enter product name: ')
        quantity = int(input('Enter quantity: '))
        date = input('Enter request date (YYY-MM-DD): ')
        total_value = float(input('Enter total value: '))

        # Insert request in database
        cursor.execute('''
        INSERT INTO requests (id_client, product_name, quantity, date, total_value)
        VALUES (?, ?, ?, ?, ?)
        ''', (id_client, product_name, quantity, date, total_value))
        conn.commit()
        print('Resquest inserted sucessufully.')

    except ValueError:
        print('-' * 80)
        print('Error: Client ID must be a integer number.')
        print('-' * 80)


# Function to perform a query with JOIN and show results
def consult_requests():
    cursor.execute('''
    SELECT
        clients.client_name, clients.email, clients.city, 
                requests.product_name, requests.quantity, requests.total_value
        FROM
            clients
        JOIN
            requests ON clients.id_client = requests.id_client
    ''')
    results = cursor.fetchall()

    # Creat and format table tp show
    table = PrettyTable(
        ['Name', 'Email', 'City', 'Product', 'Quantity', 'Total Value']
    )
    for row in results:
        table.add_row(row)
    print(table)


# Function to update an existing request
def update_request():
    try:

        # Request order ID
        id_request = int(input('Enter request ID to update: '))

        # Verify request exists
        cursor.execute(
            'SELECT * FROM requests WHERE id_request = ?', (id_request,)
        )
        request = cursor.fetchone()

        if not request:
            print('-' * 80)
            print(f'Error: Request ID {id_request} not founded.')
            print('-' * 80)
            return
        
        # Show request current data
        print('-' * 80)
        print('Request current data:')
        print(f'Product: {request[2]}')
        print(f'Quantity: {request[3]}')
        print(f'Date: {request[4]}')
        print(f'Total value: {request[5]}')
        print('-' * 80)

        # Request new order data
        product_name = input(
            'Enter new product name (Keyboard Enter to keep): '
            ) or request[2]
        quantity = input(
            'Enter new quantity (Keyboard Enter to keep): '
            ) or request[3]
        date = input(
            'Enter new date (YYYY-MM-DD) (Keyboard Enter to keep): '
        ) or request[4]
        total_value = input(
            'Enter new total value (Keyboard Enter to keep): '
        ) or request[5]

        # Update request data
        cursor.execute('''
        UPDATE requests
        SET product_name = ?, quantity = ?, date = ?, total_value = ?
        WHERE id_request = ?
        ''', (product_name, int(quantity), date, float(total_value), id_request))
        conn.commit()
        print('Update request successfully!')

    except ValueError:
        print('-' * 80)
        print('Error: Invalid input.')
        print('-' * 80)

# Interactive menu
while True:
    print('\nMenu:')
    print('1. Insert client')
    print('2. Insert request')
    print('3. Consult requests')
    print('4. Update request')
    print('5. Exit')
    option = input('Choose option (1-5): ')

    if option == '1':
        insert_client()
    elif option == '2':
        insert_request()
    elif option == '3':
        consult_requests()
    elif option == '4':
        update_request()
    elif option == '5':
        print('Shutting down system...')
        break
    else:
        print('-' * 80)
        print('Invalid option. Try again.')
        print('-' * 80)

# Close conection with database
conn.close()