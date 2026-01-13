import json
import sqlite3
from pathlib import Path
from .config import DB_PATH, PROCESSED_DATA_DIR, DASHBOARD_JSON

def export_dashboard_json():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) as total FROM transactions')
    total = cursor.fetchone()['total']
    
    cursor.execute('SELECT SUM(amount) as total_amount FROM transactions WHERE amount IS NOT NULL')
    total_amount = cursor.fetchone()['total_amount'] or 0.0
    
    cursor.execute('SELECT COUNT(DISTINCT category) as types FROM transactions')
    types = cursor.fetchone()['types']
    
    cursor.execute('SELECT MIN(date) as min_date, MAX(date) as max_date FROM transactions WHERE date IS NOT NULL')
    date_range = cursor.fetchone()
    date_range_str = f"{date_range['min_date']} to {date_range['max_date']}" if date_range['min_date'] else "N/A"
    
    cursor.execute('''
        SELECT date, name, amount, phone, category 
        FROM transactions 
        ORDER BY date DESC 
        LIMIT 50
    ''')
    recent = [dict(row) for row in cursor.fetchall()]
    
    dashboard_data = {
        "summary": {
            "totalTransactions": total,
            "totalAmount": total_amount,
            "transactionTypes": types,
            "dateRange": date_range_str
        },
        "charts": {},
        "recentTransactions": recent
    }
    
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DASHBOARD_JSON, 'w') as f:
        json.dump(dashboard_data, f, indent=2)
    
    conn.close()
    print(f"Dashboard JSON exported to {DASHBOARD_JSON}")

if __name__ == '__main__':
    export_dashboard_json()

