# 🌌 Hyperion 2024–25 — Astronomy Case Study Challenge

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/) 
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

## 📖 Overview
This repository contains the **solution framework** developed for the **Hyperion 2024–25 Astronomy Case Study Challenge**, organized by the **Astronomy Club, IIT Kanpur**.  
Hyperion is a **48-hour national challenge** where participants analyze real astrophysical data and present insights through scientific reasoning and computation.

The repo is designed to be:
- 📂 **Organized** — modular structure for datasets, code, notebooks, and reports  
- ⚡ **Reproducible** — scripts and notebooks for end-to-end analysis  
- 🔭 **Extendable** — adapt the models to any Hyperion problem statement (dark matter, GRBs, gravitational waves, etc.)

---

## 📂 Repository Structure
## 📂 Repository Structure
```text
hyperion-solution/
│
├── README.md                # Project overview (this file)
├── LICENSE                  # MIT License
├── requirements.txt         # Python dependencies
│
├── data/                    # Place datasets here
│   └── README.md
│
├── notebooks/
│   └── analysis.ipynb       # Main Jupyter Notebook
│
├── src/                     # Source code
│   ├── __init__.py
│   ├── data_loader.py       # Load and clean data
│   ├── analysis.py          # Run pipeline, visualization
│   └── modeling.py          # Astrophysical models & fitting
│
├── results/
│   ├── figures/             # Plots and figures
│   └── tables/              # Output tables
│
└── report/
    └── final_report.pdf     # Summary of methods & results

```


## ⚙️ Installation

Clone the repo:
```bash
git clone https://github.com/<your-username>/hyperion-solution.git
cd hyperion-solution
🚀 Usage

Place your dataset in the data/ folder (e.g., dataset.csv or dataset.fits).

Run the analysis pipeline:
python -m src.analysis
This generates plots in results/figures/ and prints fitted parameters.

For exploratory work, open the notebook:
jupyter notebook notebooks/analysis.ipynb
📊 Example Results

Exploratory Data Analysis: Histograms, scatter plots, and descriptive stats.

Model Fits: Example GRB lightcurve fitting, rotation curve modeling.

Figures: Saved in results/figures/.

<p align="center"> <img src="results/figures/lightcurve_peak_fit.png" alt="Lightcurve Fit" width="500"/> </p>
📄 Report

A short scientific-style report is included: report/final_report.pdf

It outlines:

Motivation & problem statement

Methodology (data, preprocessing, modeling)

Results & interpretation

Conclusion and future work

🙌 Acknowledgments

Hyperion 2024–25, organized by the Astronomy Club, IIT Kanpur

Libraries: Astropy
, SciPy
, Matplotlib

│
└── report/
└── final_report.pdf # Summary of methods & results
