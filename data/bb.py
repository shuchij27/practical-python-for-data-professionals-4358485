import pandas as pd 
import numpy as np 
import matplotlib.pyplot as mt
import seaborn as sns
import plotly.graph_objs as go
data = pd.read_csv("/workspaces/practical-python-for-data-professionals-4358485/data/BankChurners_v2.csv")
data.shape
data.head
data.columns
data['CLIENTNUM'].nunique