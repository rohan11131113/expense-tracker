from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        conn = get_db_connection()
        conn.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)',
                     (amount, category, description))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)