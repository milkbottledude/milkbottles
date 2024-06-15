import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

A = pd.read_csv('A.csv', parse_dates=True, index_col=0)