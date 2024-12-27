import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    prise INTEGER NOT NULL
    )
    """)

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_title_index ON Products(title)")

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, prise) VALUES (?, ?, ?)",
                       (f"Product{i}",
                        f"Description{i}",
                        f"{i * 100}"))

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    userneme TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def add_user(userneme, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users WHERE userneme = ?", (userneme,))

    if check_user.fetchone() is None:
        cursor.execute("INSERT INTO Users (userneme, email, age, balance) VALUES (?, ?, ?, ?)",
                       (userneme, email, age, 1000))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    check_user = cursor.execute("SELECT * FROM Users WHERE userneme = ?", (username,))
    if check_user.fetchone() is None:
        return True

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")

    products = cursor.fetchall()

    connection.commit()
    connection.close()

    return products


initiate_db()
print(get_all_products())
