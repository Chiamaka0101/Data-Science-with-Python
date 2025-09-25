import pandas as pd


bcancer_data = pd.read_csv("breast_cancer_data.csv")
# print(bcancer_data.head())
# print(bcancer_data.info)
# print(bcancer_data.describe())

#DATA CLEANING
#to handle missing values
print(bcancer_data.isnull().sum())