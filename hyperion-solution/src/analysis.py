# src/analysis.py
import os
import matplotlib.pyplot as plt
import numpy as np
from src.data_loader import load_csv, load_fits, standardize_dataframe
from src.modeling import fit_dark_matter_density, analyze_lightcurve

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results')
FIG_DIR = os.path.join(RESULTS_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

def exploratory_stats(df, prefix='df'):
    print(df.info())
    print(df.describe())
    for col in df.select_dtypes(include=[np.number]).columns[:6]:
        plt.figure()
        plt.hist(df[col].dropna(), bins=50)
        plt.title(f'{prefix} - {col}')
        plt.savefig(os.path.join(FIG_DIR, f'{prefix}_{col}.png'))
        plt.close()

def run_pipeline():
    try:
        df = load_csv('dataset.csv')
    except FileNotFoundError:
        df = load_fits('dataset.fits')

    df = standardize_dataframe(df)
    exploratory_stats(df, prefix='dataset')

    try:
        params, cov = fit_dark_matter_density(df)
        print("Fitted params:", params)
    except Exception as e:
        print("fit_dark_matter_density failed:", e)

    try:
        analyze_lightcurve(df)
    except Exception as e:
        print("analyze_lightcurve failed:", e)

if __name__ == '__main__':
    run_pipeline()
