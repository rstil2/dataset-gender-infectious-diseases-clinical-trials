import pandas as pd
from pathlib import Path

def preprocess_data(raw_path: Path, processed_path: Path) -> None:
    """Raw Data → Preprocessing"""
    df = pd.read_csv(raw_path)
    
    # Clean data
    df["female_pct"] = (df["Female N"] / df["Total N"]) * 100
    df = df.dropna(subset=["Locations"])
    
    # Save processed data
    df.to_csv(processed_path, index=False)

if __name__ == "__main__":
    raw_path = Path("data/raw/clinical_trials.csv")
    processed_path = Path("data/processed/processed_clinical_trials.csv")
    preprocess_data(raw_path, processed_path)
