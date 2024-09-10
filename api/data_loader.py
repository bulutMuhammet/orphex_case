# app_name/data_loader.py

import pandas as pd
import os

def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(BASE_DIR, 'data/mockupinterviewdata.csv')
    return pd.read_csv(csv_path)

df = load_data()