# Crime Data Explorer

A minimal project for analyzing public safety / crime incident data.  
It loads a CSV, normalizes dates & categories, and outputs two plots:

- **Monthly incidents** → `out/incidents_by_month.png`  
- **Top categories** → `out/top_categories.png`  

---

## Why it matters
Agencies like the FBI, CIA, and DHS use similar workflows daily: cleaning messy data, spotting trends, and producing actionable insights.  
This repo shows applied math + coding skills on real-world open data.

---

## Quickstart
git clone https://github.com/Neuer2718/crime-explorer.git  
cd crime-explorer  
python3 -m venv .venv && source .venv/bin/activate  
pip install -r requirements.txt  
python crime_explorer.py --csv sample_crime.csv  

Plots will be saved in `out/`.

---

## Next Steps
--since YYYY-MM        # filter by time  
--area BOROUGH         # filter by area  
# Export report.csv with monthly counts  
# Optional: Streamlit dashboard  

---

🚀 Demonstrates core skills for public safety + intelligence analysis.
