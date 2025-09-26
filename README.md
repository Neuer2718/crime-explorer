# Crime Data Explorer

Minimal but practical project that analyzes **open crime / incident datasets** (CSV format).  
This project demonstrates data cleaning, normalization, and visualization of public safety data — skills directly relevant to FBI, CIA, DHS, and local government analysts.

---

## Why this matters
Agencies and law enforcement analysts often work with **messy, inconsistent public safety data**.  
This project shows how to:
- Normalize different schema conventions (date, category, borough/area).  
- Produce quick, reproducible insights with Python.  
- Communicate findings visually for decision-makers.  

---

## Features
- **Data ingestion**: Reads any CSV with crime/incident records.  
- **Date normalization**: Handles multiple common column names (`occurred_at`, `incident_date`, `Created Date`, etc.).  
- **Category aggregation**: Groups incident categories for easy analysis.  
- **Visualizations**:
  - Monthly trend of incidents → `out/incidents_by_month.png`
  - Top incident categories → `out/top_categories.png`

---

## Usage

### 1. Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
