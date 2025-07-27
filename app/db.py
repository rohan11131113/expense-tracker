import sqlite3

conn = sqlite3.connect('expenses.db')
conn.execute('''CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT
)''')
conn.commit()
conn.close()
