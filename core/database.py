import sqlite3
import os
from datetime import datetime
from rich.table import Table
from rich.console import Console

DB_PATH = "database/cyberos.db"

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module TEXT,
            target TEXT,
            status TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_action(module, target, status="SUCCESS"):
    try:
        init_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO audit_logs (module, target, status, timestamp) VALUES (?, ?, ?, ?)",
                       (module, target, status, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
    except Exception:
        pass

def show_audit_logs():
    console = Console()
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, module, target, status, timestamp FROM audit_logs ORDER BY id DESC LIMIT 15")
    rows = cursor.fetchall()
    conn.close()

    table = Table(title="[bold red]CyberOS v7 - Security Audit Logs[/bold red]", header_style="bold cyan", border_style="bright_red")
    table.add_column("ID", style="dim", justify="center")
    table.add_column("Module", style="green")
    table.add_column("Target / Input", style="yellow")
    table.add_column("Status", style="magenta")
    table.add_column("Timestamp", style="dim white")

    for row in rows:
        table.add_row(str(row[0]), row[1], row[2], row[3], row[4])
    
    console.print(table)
