# Personal Expense Tracker
A full-stack web application to manage personal expenses, track spending patterns,
and visualize financial data with interactive charts and summaries.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation & Setup](#installation--setup)

## Project Overview
This project helps users efficiently manage their personal expenses. Users can add,
edit, delete, and view their expenses. It also provides summaries, charts, 
and budget alerts to help make better financial decisions.

## Features

### Phase 1 – Core Features
- Add expense with success notification.
- View all expenses in a sortable table (by date and amount).
- Edit or delete expenses.
- Monthly and yearly summaries.
- Total expenses till now.

### Phase 2 – Enhanced Features
- Search expenses by description.
- Filter expenses by category.
- Budget alerts for overspending.
- Pie chart (category-wise expense distribution).
- Line chart (monthly expenses trend).
- Category-wise total expenditure.

### Phase 3 – Advanced / Placement-Ready Features
- User login/signup with password encryption.
- Recurring expenses management.
- Export reports (PDF/Excel).
- Trend analysis and predictions.
- Multi-filter search (date range + category + amount + description).
- Responsive dashboard with interactive charts and notifications.
- Secure backend with validation and error handling.

## Technologies Used
- Backend: Flask, Python
- Frontend: HTML5, CSS3, JavaScript, Bootstrap/TailwindCSS
- Database: SQLite / PostgreSQL
- Charts & Visualization: Chart.js
- Deployment: Render / Heroku / Railway

## Installation & Setup

Clone the repository:
```bash
git clone https://github.com/Gitanjali7890/Personal_Expense_Tracker.git
cd personal-expense-tracker
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
flask run



  

