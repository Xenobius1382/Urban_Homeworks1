# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

# Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3

# Задача "Первые пользователи"

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

# Заполняем таблицу пользователями
#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
#               (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))

# Обновляем значение баланса в каждой второй строке
#for i in range(1, 11, 2):
#    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

# Удаляем каждую третью строку
#for i in range(1, 11, 3):
#    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}", ))

# Выводим в консоль все строки где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()

