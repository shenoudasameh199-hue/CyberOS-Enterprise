import sqlite3
import json
from datetime import datetime

DB_PATH = "database/cyberos.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            module TEXT NOT NULL,
            target TEXT NOT NULL,
            status TEXT NOT NULL,
            details TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_event(module, target, status, details=None):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    details_str = json.dumps(details) if isinstance(details, (dict, list)) else str(details or "")
    cursor.execute('''
        INSERT INTO audit_logs (timestamp, module, target, status, details)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, module, target, status, details_str))
    conn.commit()
    conn.close()

# Alias لتوافق الموديولات القديمة التي تستدعي log_action
log_action = log_event

def get_logs(limit=10):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, timestamp, module, target, status FROM audit_logs ORDER BY id DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
