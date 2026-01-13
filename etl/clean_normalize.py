import re
from datetime import datetime
from typing import Dict, Any, Optional
from dateutil import parser as date_parser

def normalize_phone(phone: Optional[str]) -> Optional[str]:
    if not phone:
        return None
    cleaned = re.sub(r'[^\d+]', '', phone)
    if len(cleaned) >= 9:
        if cleaned.startswith('250'):
            return cleaned
        elif cleaned.startswith('0'):
            return '250' + cleaned[1:]
        else:
            return '250' + cleaned
    return None

def normalize_date(date_str: Optional[str]) -> Optional[str]:
    if not date_str:
        return None
    try:
        dt = date_parser.parse(date_str)
        return dt.isoformat()
    except (ValueError, TypeError):
        return None

def clean_transaction(transaction: Dict[str, Any]) -> Dict[str, Any]:
    cleaned = transaction.copy()
    
    phone = transaction.get('phone')
    cleaned['phone'] = normalize_phone(phone)
    
    date = transaction.get('date')
    cleaned['date'] = normalize_date(date)
    
    return cleaned

