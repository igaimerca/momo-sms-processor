# MoMo SMS Data Processor

## Team Information

**Team Name:** Techie

**Team Members:**
- Aime Igirimpuhwe

## Project Description

This fullstack application processes Mobile Money (MoMo) SMS data in XML format. The system cleans and categorizes data, stores it in a relational database, and provides a frontend interface for data analysis and visualization.

### Key Features
- XML data parsing and extraction
- Data cleaning and normalization
- Transaction categorization
- SQLite database storage
- Interactive dashboard for data visualization
- RESTful API

## System Architecture

[View Architecture Diagram on Miro](https://miro.com/app/board/uXjVGRfqY5s=/?share_link_id=998925664556)

[Architecture Diagram (in repo)](docs/architecture.md)

The system follows a modular ETL (Extract, Transform, Load) architecture with the following components:

### Architecture Components:

1. **Data Input**: XML files containing MoMo SMS transaction data
2. **ETL Pipeline**: 
   - Parse XML using ElementTree/lxml
   - Clean and normalize data (amounts, dates, phone numbers)
   - Categorize transactions using rule-based classification
   - Load into SQLite database
3. **Data Storage**: SQLite relational database
4. **Frontend**: Static HTML/CSS/JavaScript dashboard
5. **API Layer**: FastAPI REST endpoints 

## Project Structure

```
.
├── README.md                         # Setup, run, overview
├── .env.example                      # DATABASE_URL or path to SQLite
├── requirements.txt                  # Python dependencies
├── index.html                        # Dashboard entry (static)
├── web/
│   ├── styles.css                    # Dashboard styling
│   ├── chart_handler.js              # Fetch + render charts/tables
│   └── assets/                       # Images/icons (optional)
├── data/
│   ├── raw/                          # Provided XML input (git-ignored)
│   │   └── momo.xml
│   ├── processed/                    # Cleaned/derived outputs for frontend
│   │   └── dashboard.json            # Aggregates the dashboard reads
│   ├── db.sqlite3                    # SQLite DB file
│   └── logs/
│       ├── etl.log                   # Structured ETL logs
│       └── dead_letter/              # Unparsed/ignored XML snippets
├── etl/
│   ├── __init__.py
│   ├── config.py                     # File paths, thresholds, categories
│   ├── parse_xml.py                  # XML parsing (ElementTree/lxml)
│   ├── clean_normalize.py            # Amounts, dates, phone normalization
│   ├── categorize.py                 # Simple rules for transaction types
│   ├── load_db.py                    # Create tables + upsert to SQLite
│   └── run.py                        # CLI: parse -> clean -> categorize -> load -> export JSON
├── api/                              # Optional (bonus)
│   ├── __init__.py
│   ├── app.py                        # Minimal FastAPI with /transactions, /analytics
│   ├── db.py                         # SQLite connection helpers
│   └── schemas.py                    # Pydantic response models
├── scripts/
│   ├── run_etl.sh                    # python etl/run.py --xml data/raw/momo.xml
│   ├── export_json.sh                # Rebuild data/processed/dashboard.json
│   └── serve_frontend.sh             # python -m http.server 8000 (or Flask static)
└── tests/
    ├── test_parse_xml.py             # Small unit tests
    ├── test_clean_normalize.py
    └── test_categorize.py
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/igaimerca/momo-sms-processor.git
cd momo-sms-processor
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment file:
```bash
cp .env.example .env
```

5. Update `.env` with your database path if needed.

## Running the Application

### ETL Pipeline
```bash
./scripts/run_etl.sh
```

### Export Dashboard Data
```bash
./scripts/export_json.sh
```

### Serve Frontend
```bash
./scripts/serve_frontend.sh
```

Then open `http://localhost:8000` in your browser.

## Scrum Board

[View our Scrum Board](https://trello.com/b/TQnNW4nd/momo-sms-processor)

## Contributing
Please follow the project structure and coding standards.
