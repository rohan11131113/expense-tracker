import sqlite3

conn = sqlite3.connect('expenses.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("Database and table created successfully.")
