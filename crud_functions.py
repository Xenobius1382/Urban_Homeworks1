import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


def get_connection():
    return sqlite3.connect('not_telegram.db')

def initiate_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price REAL
            )
        ''')
        conn.commit()

def get_all_products():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        return rows



cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for i in range(1, 5):
#    cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
#               (f"Продукт {i}", f"Описание {i}", f"{i*100}"))



connection.commit()
connection.close()
