# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean = sale_price.mean()
    median = sale_price.median()
    m = sale_price.mode()
    mode = m[0]
    return (mean, median, mode)

calculate_statistics()
