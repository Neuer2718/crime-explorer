import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATE_CANDIDATES = [
    "occurred_at", "incident_datetime", "incident_date", "date", "reported_date",
    "Occurred On Date", "DateOccurred", "OccurredDate", "Created Date"
]
CAT_CANDIDATES = [
    "category", "offense_category", "offense", "offense_type",
    "primary_type", "incident_type", "complaint_type", "Crime type"
]
BORO_CANDIDATES = ["borough", "boro", "neighborhood", "precinct", "district"]

def find_col(df: pd.DataFrame, candidates: list[str]) -> str | None:
    cols = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in cols:
            return cols[cand.lower()]
    return None

def load_data(path: str | None) -> pd.DataFrame:
    if path and Path(path).exists():
        return pd.read_csv(path, low_memory=False)
    if Path("sample_crime.csv").exists():
        return pd.read_csv("sample_crime.csv", low_memory=False)
    raise FileNotFoundError("Provide --csv path or include sample_crime.csv")

def normalize(df: pd.DataFrame) -> pd.DataFrame:
    date_col = find_col(df, DATE_CANDIDATES)
    if not date_col:
        raise ValueError("Could not find a date column. Add one of: " + ", ".join(DATE_CANDIDATES))
    df["date"] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=["date"])

    cat_col = find_col(df, CAT_CANDIDATES)
    if cat_col:
        df["category"] = df[cat_col].astype(str).str.strip()
    else:
        df["category"] = "Unknown"

    boro_col = find_col(df, BORO_CANDIDATES)
    if boro_col:
        df["area"] = df[boro_col].astype(str).str.strip()

    return df

def plot_monthly(df: pd.DataFrame, out_png: str):
    monthly = df["date"].dt.to_period("M").dt.to_timestamp().value_counts().sort_index()
    Path(out_png).parent.mkdir(parents=True, exist_ok=True)
    plt.figure()
    monthly.plot(kind="line", marker="o")
    plt.title("Incidents per Month")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def plot_top_categories(df: pd.DataFrame, out_png: str, k: int = 10):
    top = df["category"].value_counts().head(k)
    Path(out_png).parent.mkdir(parents=True, exist_ok=True)
    plt.figure()
    top.plot(kind="bar")
    plt.title(f"Top {k} Incident Categories")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def main():
    ap = argparse.ArgumentParser(description="Crime/Open-Data Explorer")
    ap.add_argument("--csv", help="Path to CSV (optional). If omitted, uses sample_crime.csv")
    ap.add_argument("--outdir", default="out", help="Output directory for plots")
    ap.add_argument("--topk", type=int, default=10, help="Top categories to show")
    args = ap.parse_args()

    df_raw = load_data(args.csv)
    df = normalize(df_raw)

    print(f"Rows: {len(df):,}")
    print("Date range:", df["date"].min().date(), "→", df["date"].max().date())
    print("Unique categories:", df["category"].nunique())

    plot_monthly(df, f"{args.outdir}/incidents_by_month.png")
    plot_top_categories(df, f"{args.outdir}/top_categories.png", k=args.topk)
    print(f"Wrote: {args.outdir}/incidents_by_month.png and {args.outdir}/top_categories.png")

if __name__ == "__main__":
    main()             