import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_plots(data_path: Path, fig_dir: Path) -> None:
    """Validation → Visualization"""
    df = pd.read_csv(data_path)
    
    # Temporal trends
    plt.figure(figsize=(10, 6))
    for disease in df["disease"].unique():
        subset = df[df["disease"] == disease]
        plt.plot(subset["year"], subset["female_pct"], label=disease, marker="o")
    
    plt.title("Female Participation Rates (1994–2022)")
    plt.savefig(fig_dir / "temporal_trends.png")

if __name__ == "__main__":
    data_path = Path("data/processed/processed_clinical_trials.csv")
    fig_dir = Path("figures")
    fig_dir.mkdir(exist_ok=True)
    generate_plots(data_path, fig_dir)
