from typing import Dict, Any
from .config import TRANSACTION_CATEGORIES

def categorize_transaction(transaction: Dict[str, Any]) -> str:
    body = transaction.get('body', '').lower()
    
    for category, keywords in TRANSACTION_CATEGORIES.items():
        if category == "other":
            continue
        if any(keyword in body for keyword in keywords):
            return category
    
    return "other"

