import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")



# Удаляем пользователя с id равным 6
#cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))

# Подсчет общего количества записей в базе
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# средний баланс всех пользователей
print(all_balances/total_users)

connection.commit()
connection.close()