import typer
import sqlite3
from tabulate import tabulate
from typing import Optional
from datetime import datetime
import re


app = typer.Typer()

# SQLite connection
conn = sqlite3.connect("employee_absent.db")
cursor = conn.cursor()

def is_valid_employee_id(employee_id: str) -> bool:
    pattern = r'^NS-\d{2}-\d{3}$'
    return bool(re.match(pattern, employee_id))

def is_valid_date(date_string: str) -> bool:
    date_format = "%B %d, %Y"
    
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    employee_id TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS absent (
    id INTEGER PRIMARY KEY,
    employee_id TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
)
""")

@app.command()
def add_employee(first_name: str, last_name: str, employee_id: str):
    """
    Add a new employee to the database
    """
    if not is_valid_employee_id(employee_id):
        typer.echo("Employee ID is invalid.")
    else:
        try:
            cursor.execute("INSERT INTO employees (first_name, last_name, employee_id) VALUES (?, ?, ?)", (first_name, last_name, employee_id))
            conn.commit()
            typer.echo(f"Employee {first_name} {last_name} with ID {employee_id} added successfully.")
        except sqlite3.IntegrityError:
            typer.echo(f"Employee with ID {employee_id} already exists.")

@app.command()
def add_absent(employee_id: str, date: Optional[str]=None):
    """
    Add absent for an employee
    """
    if date and not is_valid_date(date):
        typer.echo(f"The provided date is not valid. Expected format is [May 01, 2023].")
    else:
        if not date:
            date = datetime.now().strftime('%B %d, %Y')

        cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
        employee = cursor.fetchone()

        if employee is None:
            typer.echo(f"Employee with ID {employee_id} not found.")
        else:
            cursor.execute("SELECT * FROM absent WHERE employee_id = ? AND date = ?", (employee_id, date,))
            absent = cursor.fetchone()
            if absent:
                typer.echo(f"An absent has already been added for the {employee_id} for {date}")
            else:
                cursor.execute("INSERT INTO absent (employee_id, date) VALUES (?, ?)", (employee_id, date))
                conn.commit()
                typer.echo(f"Absent for employee with ID {employee_id} on {date} added successfully.")

@app.command()
def delete_absent(employee_id: str, date: Optional[str]=None):
    """
    Delete absent for an employee
    """
    if date and not is_valid_date(date):
        typer.echo(f"The provided date is not valid. Expected format is [May 01, 2023].")
    else:
        if not date:
            date = datetime.now().strftime('%B %d, %Y')

        cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
        employee = cursor.fetchone()

        if employee is None:
            typer.echo(f"Employee with ID {employee_id} not found.")
        else:
            cursor.execute("DELETE FROM absent WHERE employee_id = ? AND date = ?", (employee_id, date,))
            conn.commit()
            typer.echo(f"Absent for employee with ID {employee_id} on {date} deleted successfully.")

@app.command()
def list_employees(month: Optional[str] = None):
    """
    List all employees and their absent
    """
    if not month:
        month = datetime.now().strftime('%B')
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.execute(f"""
    SELECT employee_id, COUNT(*) as absent_count
    FROM absent
    WHERE date LIKE '%{month}%'
    GROUP BY employee_id
    """)
    absents = cursor.fetchall()
    absent_dict = {absent[0]: absent[1] for absent in absents}

    table_data = []
    for employee in employees:
        row = [
            employee[3],
            employee[1] + ' ' + employee[2],
            absent_dict.get(employee[3], 0)
        ]
        table_data.append(row)

    headers = ["Employee ID", "Name", "Absent Count"]
    typer.echo(tabulate(table_data, headers=headers, tablefmt="pretty"))

@app.command()
def list_absents(employee_id: str, month: str):
    """
    List all employees and their absent
    """
    if not month:
        month = datetime.now().strftime('%B')
    cursor.execute(f"SELECT * FROM absent WHERE employee_id = '{employee_id}' AND date LIKE '%{month}%'")
    absents = cursor.fetchall()

    table_data = []
    for absent in absents:
        row = [
            absent[2],
        ]
        table_data.append(row)

    headers = [f"{employee_id}"]
    typer.echo(tabulate(table_data, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    app()

