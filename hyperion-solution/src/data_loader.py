# src/data_loader.py
import os
import pandas as pd
import numpy as np
from astropy.table import Table

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    return pd.read_csv(path)

def load_fits(filename):
    path = os.path.join(DATA_DIR, filename)
    table = Table.read(path)
    return table.to_pandas()

def standardize_dataframe(df):
    df = df.copy()
    df = df.dropna(how='all')
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except:
                pass
    return df
