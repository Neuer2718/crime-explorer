# Crime Data Explorer

This is a minimal but practical project that explores public safety / crime incident data.  
It loads a CSV file (either the included `sample_crime.csv` or a real dataset), normalizes the date and category fields, and produces two simple visualizations:

- out/incidents_by_month.png → monthly trend of incidents  
- out/top_categories.png → top incident categories  

---

## Why this matters (Gov/Cyber Relevance)

Agencies like the FBI, CIA, DHS, and local law enforcement all analyze messy incident data daily:  
- Identifying trends over time (e.g., rising crime categories, seasonal spikes).  
- Comparing incident categories across locations.  
- Producing quick, visual insights that inform policy or investigations.  

This project demonstrates the ability to:  
- Ingest and clean real-world structured data.  
- Normalize inconsistent schemas.  
- Generate reproducible, interpretable analysis artifacts.  

---

## Features
- Robust column detection: Handles various date/category/area column names common in open datasets.  
- Summary statistics: Prints row count, date range, and unique categories.  
- Visualizations:  
  - Monthly incident trend (line chart).  
  - Top incident categories (bar chart).  
- Simple CLI: Runs from the terminal with a few flags.

---

## Usage

### 1. Clone and set up environment
git clone https://github.com/Neuer2718/crime-explorer.git
cd crime-explorer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 2. Run with included sample data
python crime_explorer.py

### 3. Run with a real dataset
python crime_explorer.py --csv /path/to/real_crime_data.csv

### 4. Output
# Console prints dataset stats
# Plots saved in out/
ls out/

---

## Example Output
Rows: 6  
Date range: 2022-01-15 → 2022-03-29  
Unique categories: 3  
Wrote: out/incidents_by_month.png and out/top_categories.png  

---

## Next Steps (Future Enhancements)
--since YYYY-MM        # filter incidents by date range  
--area <borough>       # filter by borough/district  
# Export report.csv with counts by month/category  
# Add Streamlit dashboard for interactive exploration  

---

This project demonstrates applied data analysis skills that map directly to public safety + intelligence analysis work.
