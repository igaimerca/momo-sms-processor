from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .db import get_db_connection
from .schemas import Transaction, Analytics

app = FastAPI(title="MoMo SMS Data API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/transactions", response_model=List[Transaction])
async def get_transactions(limit: int = 100):
    conn = get_db_connection()
    conn.row_factory = lambda cursor, row: {
        'id': row[0],
        'body': row[1],
        'name': row[2],
        'phone': row[3],
        'date': row[4],
        'amount': row[5],
        'category': row[6],
        'type': row[7]
    }
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions LIMIT ?', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/analytics", response_model=Analytics)
async def get_analytics():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*), SUM(amount) FROM transactions')
    result = cursor.fetchone()
    conn.close()
    return {
        "total_transactions": result[0] or 0,
        "total_amount": result[1] or 0.0
    }

