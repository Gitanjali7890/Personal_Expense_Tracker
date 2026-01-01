# --------import database, flask and os--------
from flask import Flask, render_template, request, redirect, flash
import sqlite3
from datetime import date as dt_date
import os

#------ call flask-------
app = Flask(__name__)
#----- add secret key for printing message-------
app.secret_key = "secret123"

# ---------- DATABASE ----------
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
            description TEXT,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- ROUTES ----------

@app.route('/')     #------ route for home-----
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])    #----route for add expenses----
def add_expense():
    if request.method == 'POST':
        title = request.form.get('title')
        amount = request.form.get('amount')
        description = request.form.get('description')
        expense_date = request.form.get('date')
        category = request.form.get('category')

        if not title or not amount or not expense_date or not category:
            flash("❌ Please fill all required fields")    #---required fill msg for field----
            return redirect('/add')
       

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO expenses (title, amount, date, description, category) VALUES (?, ?, ?, ?, ?)",
            (title, amount, expense_date, description, category)
        )
        conn.commit()
        conn.close()

        flash("✅ Expense added successfully!")       #---flask message using secret key----
        return redirect('/add')

    return render_template('add_expense.html')

@app.route('/view')           #----route for view all -----
def view_expenses():
    sort = request.args.get('sort')
    category = request.args.get('category')

    query = "SELECT * FROM expenses"
    params = []

    if category:
        query += " WHERE category = ?"
        params.append(category)

    if sort == 'date':
        query += " ORDER BY date DESC"
    elif sort == 'amount_high':
        query += " ORDER BY amount DESC"
    elif sort == 'amount_low':
        query += " ORDER BY amount ASC"

    conn = get_db_connection()
    expenses = conn.execute(query, params).fetchall()
    conn.close()

    return render_template('View_all.html', expenses=expenses)

@app.route('/delete/<int:id>', methods=['POST'])        #-----delete button route in view all-----
def delete_expense(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/view')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])      #-----edit button route in view all-----
def edit_expense(id):
    conn = get_db_connection()

    if request.method == 'POST':
        conn.execute("""
            UPDATE expenses
            SET title=?, amount=?, date=?, description=?, category=?
            WHERE id=?
        """, (
            request.form['title'],
            request.form['amount'],
            request.form['date'],
            request.form['description'],
            request.form['category'],
            id
        ))
        conn.commit()
        conn.close()
        return redirect('/view')

    expense = conn.execute("SELECT * FROM expenses WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template('edit.html', expense=expense)

@app.route('/summary')          #----route for summary 
def summary():
    today = dt_date.today()
    month = today.strftime('%Y-%m')
    year = today.strftime('%Y')

    conn = get_db_connection()
    monthly = conn.execute(
        "SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', date)=?",
        (month,)
    ).fetchone()[0] or 0

    yearly = conn.execute(
        "SELECT SUM(amount) FROM expenses WHERE strftime('%Y', date)=?",
        (year,)
    ).fetchone()[0] or 0

    conn.close()

    return render_template('summary.html', monthly_total=monthly, yearly_total=yearly)

@app.route('/total')             #-------route for total------
def total():
    conn = get_db_connection()
    total = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0] or 0
    conn.close()
    return render_template('total.html', total=total)


# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
