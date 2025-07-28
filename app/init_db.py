import sqlite3

conn = sqlite3.connect('app/expenses.db')  # ensure this path matches what's used in app.py
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
