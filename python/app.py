from flask import Flask, render_template, request, redirect, flash
import sqlite3

from datetime import date
import os


app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = "secrect123"   #secrect key is addded o show the message

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()
app = Flask(__name__)
app.secret_key = "secrect123"
init_db()

@app.route('/')
def about():
    return render_template('index.html')   # to show the index page at first
@app.route('/view')
def view_expenses():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall() 
    sort = request.args.get('sort')

    conn = get_db_connection()

    if sort == 'date':
        expenses = conn.execute(
            'SELECT * FROM expenses ORDER BY date DESC'
        ).fetchall()

    elif sort == 'amount_high':
        expenses = conn.execute(
            'SELECT * FROM expenses ORDER BY amount DESC'
        ).fetchall()

    elif sort == 'amount_low':
        expenses = conn.execute(
            'SELECT * FROM expenses ORDER BY amount ASC'
        ).fetchall()

    else:
        expenses = conn.execute(
            'SELECT * FROM expenses'
        ).fetchall()

      # for view all expenditure
    conn.close()
    return render_template('View_all.html', expenses=expenses)
@app.route('/summary')
def summary():
    conn = get_db_connection()

    today = date.today()
    current_month = today.strftime('%Y-%m')
    current_year = today.strftime('%Y')

    # Total for current month
    monthly_total = conn.execute(
        """
        SELECT SUM(amount) FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        """,
        (current_month,)
    ).fetchone()[0]

    # Total for current year
    yearly_total = conn.execute(
        """
        SELECT SUM(amount) FROM expenses
        WHERE strftime('%Y', date) = ?
        """,
        (current_year,)
    ).fetchone()[0]

    conn.close()

    # Handle None values
    monthly_total = monthly_total or 0
    yearly_total = yearly_total or 0

    return render_template(
        'summary.html',
        monthly_total=monthly_total,
        yearly_total=yearly_total
    )
# for deleting an expense
@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/view')

#for total amount expend till now
@app.route('/total')
def total_expense():
    conn = get_db_connection()
    total = conn.execute('SELECT SUM(amount) FROM expenses').fetchone()[0]
    conn.close()

    if total is None:
        total = 0

    return render_template('total.html', total=total)
#to add new expense
@app.route('/add', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        title = request.form['title']
        amount = request.form['amount']
        description = request.form['description']
        date = request.form['date']
        conn.execute(
            'INSERT INTO expenses (title, amount, description,date) VALUES (?, ?,?,?)',
            (title, amount,description,date)
        )
        conn.commit()
        conn.close()
        # message after adding expense
        flash("✅ Expense added successfully!")
        return redirect('/add')

    conn.close()
    return render_template('add_expense.html')
#edit option
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    conn = get_db_connection()

    if request.method == 'POST':
        title = request.form['title']
        amount = request.form['amount']
        date = request.form['date']
        description = request.form['description']

        conn.execute("""
            UPDATE expenses
            SET title = ?, amount = ?, date = ?, description = ?
            WHERE id = ?
        """, (title, amount, date, description, id))

        conn.commit()
        conn.close()
        return redirect('/view')

    expense = conn.execute(
        'SELECT * FROM expenses WHERE id = ?', (id,)
    ).fetchone()

    conn.close()
    return render_template('edit.html', expense=expense)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
