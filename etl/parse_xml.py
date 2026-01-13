import xml.etree.ElementTree as ET
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

def extract_name(body: str) -> Optional[str]:
    patterns = [
        r'transferred to ([A-Z][A-Z\s]+) \(',
        r'received.*from ([A-Z][A-Z\s]+) \(',
        r'payment.*to ([A-Z][A-Z\s]+)',
        r'from ([A-Z][A-Z\s]+) \(',
    ]
    for pattern in patterns:
        match = re.search(pattern, body)
        if match:
            name = match.group(1).strip()
            if len(name) > 2:
                return name
    return None

def extract_phone(body: str) -> Optional[str]:
    patterns = [
        r'\((\d{12})\)',
        r'\((\d{9,12})\)',
        r'(\+?\d{10,15})',
        r'(\*{3,}\d{3})',
    ]
    for pattern in patterns:
        match = re.search(pattern, body)
        if match:
            phone = match.group(1)
            cleaned = re.sub(r'[^\d+]', '', phone)
            if len(cleaned) >= 9:
                return cleaned
    return None

def extract_amount(body: str) -> Optional[float]:
    patterns = [
        r'(\d{1,3}(?:,\d{3})*(?:\.\d+)?)\s*RWF',
        r'(\d+(?:,\d{3})*(?:\.\d+)?)\s*RWF',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, body)
        if matches:
            try:
                amount_str = matches[0].replace(',', '')
                return float(amount_str)
            except ValueError:
                continue
    return None

def extract_date(body: str) -> Optional[str]:
    pattern = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})'
    match = re.search(pattern, body)
    if match:
        return match.group(1)
    return None

def parse_xml_file(xml_path: Path) -> List[Dict[str, Any]]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    transactions = []
    for sms in root.findall('.//sms'):
        body = sms.findtext('body', '')
        
        transaction = {
            'body': body,
            'name': extract_name(body),
            'phone': extract_phone(body),
            'amount': extract_amount(body),
            'date': extract_date(body),
        }
        transactions.append(transaction)
    
    return transactions

