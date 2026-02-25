import sqlite3
from datetime import datetime

#  подключение к базе данных
connect = sqlite3.connect('users_base.db')
cursor = connect.cursor()
cursor.execute('SELECT name,email,registration_date FROM users')
for user in cursor.fetchall():
    print(f'Имя: {user[0]}, email: {user[1]}, дата регистрации: {(user[2])}')

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute('INSERT INTO users (name, email, registration_date) VALUES (?, ?, ?)', ('John Doe', 'john@example.com', current_date))
connect.commit()    

# фильтрация вывода
cursor.execute('SELECT name,email,registration_date FROM users WHERE registration_date > ?', ('2024-01-01 00:00:00',))
for user in cursor.fetchall():
    print(f'Имя: {user[0]}, email: {user[1]}, дата регистрации: {(user[2])}')
connect.close()