import sqlite3
from pathlib import Path
from typing import List, Dict, Any
from .config import DB_PATH

def create_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            body TEXT,
            name TEXT,
            phone TEXT,
            date TEXT,
            amount REAL,
            category TEXT,
            type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    try:
        cursor.execute('ALTER TABLE transactions ADD COLUMN name TEXT')
    except sqlite3.OperationalError:
        pass
    conn.commit()

def upsert_transactions(transactions: List[Dict[str, Any]]):
    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)
    
    cursor = conn.cursor()
    for tx in transactions:
        cursor.execute('''
            INSERT OR REPLACE INTO transactions 
            (body, name, phone, date, amount, category, type)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            tx.get('body'),
            tx.get('name'),
            tx.get('phone'),
            tx.get('date'),
            tx.get('amount'),
            tx.get('category'),
            tx.get('type')
        ))
    
    conn.commit()
    conn.close()

