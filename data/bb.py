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
data.isnull().sum()
data = data [['CLIENTNUM', 'Attrition_Flag', 'Customer_Age', 'Gender',
            'Dependent_count', 'Education_Level', 'Marital_Status',
            'Income_Category', 'Card_Category', 'Months_on_book',
            'Total_Relationship_Count', 'Months_Inactive_12_mon',
            'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
            'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
            'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']]

data.columns
data.dtypes
