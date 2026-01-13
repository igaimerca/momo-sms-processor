import argparse
import sys
from pathlib import Path
from .parse_xml import parse_xml_file
from .clean_normalize import clean_transaction
from .categorize import categorize_transaction
from .load_db import upsert_transactions
from .config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def main():
    parser = argparse.ArgumentParser(description='Run ETL pipeline for MoMo SMS data')
    parser.add_argument('--xml', type=str, default=str(RAW_DATA_DIR / 'momo.xml'),
                       help='Path to XML file')
    args = parser.parse_args()
    
    xml_path = Path(args.xml)
    if not xml_path.exists():
        print(f"Error: XML file not found at {xml_path}")
        sys.exit(1)
    
    print("Parsing XML...")
    transactions = parse_xml_file(xml_path)
    print(f"Parsed {len(transactions)} transactions")
    
    print("Cleaning and normalizing...")
    cleaned = [clean_transaction(tx) for tx in transactions]
    
    print("Categorizing...")
    for tx in cleaned:
        tx['category'] = categorize_transaction(tx)
    
    print("Loading into database...")
    upsert_transactions(cleaned)
    print("ETL pipeline completed successfully!")

if __name__ == '__main__':
    main()

