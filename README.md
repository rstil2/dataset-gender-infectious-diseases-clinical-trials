# Gender Disparities in Infectious Disease Clinical Trials (1994–2022)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A reproducible workflow for analyzing female participation rates in clinical trials for COVID-19, Ebola, and HIV.  

---

## Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/trial_gender_dataset.git
cd trial_gender_dataset
```

### 2. Create Conda Environment
```bash
conda env create -f environment.yml
conda activate trial_analysis
```

---

## Usage

Run scripts **in order** to reproduce the analysis:

```bash
# 1. Preprocess raw data
python src/1_preprocessing.py

# 2. Run Bayesian hierarchical model
python src/2_bayesian_model.py

# 3. Validate model outputs
python src/3_validation.py

# 4. Generate publication-ready figures
python src/4_visualization.py
```

---

## Repository Structure

```
trial_gender_dataset/
├── data/
│   ├── raw/                   # Original data (clinical_trials.csv)
│   └── processed/             # Cleaned data (auto-generated)
├── src/
│   ├── 1_preprocessing.py     # Data cleaning and validation
│   ├── 2_bayesian_model.py    # Statistical analysis
│   ├── 3_validation.py        # Model diagnostics
│   └── 4_visualization.py     # Figure generation
├── results/                   # Model outputs (traces, metrics)
├── figures/                   # Generated plots (PNG/PDF)
├── environment.yml            # Conda environment
└── README.md                  # This file
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Citation

If you use this dataset or code, please cite:  
```bibtex
@article{stillwell_2025,  
  author = {Stillwell, R.C.},  
  title = {Gender Disparities in Clinical Trials: A Bayesian Analysis of Temporal Trends},  
  journal = {BMJ Public Health},  
  year = {In Review},  
  doi = {10.XXXX/YYYYYYY}  
}
```

---

## Contact  
For questions or support: [craig.stillwell@gmail.com](mailto:craig.stillwell@gmail.com)  
Project URL: [https://github.com/rstil2/dataset-gender-infectious-diseases-clinical-trials](https://github.com/rstil2/dataset-gender-infectious-diseases-clinical-trials)
