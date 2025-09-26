import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



#load dataset
fraud_detection_data = pd.read_csv("bank_fraud_detect.csv")


#take a peek
# print(fraud_detection_data)


# PRINT SUMMARY INFO: COLUMN NAMES, NON-NULL COUNTS, DATA TYPES, MEMORY USAGE
# print(fraud_detection_data.info)


#SHOW FIRST AND LAST VALUES
# print(fraud_detection_data.head())
# print(fraud_detection_data.tail())


# PRINT STATS (count, mean, std, min, max, etc.)
# print(fraud_detection_data.describe())
# print(fraud_detection_data.shape) 


#FIND MISSING VALUES
# print(fraud_detection_data.isnull().sum()) #there are no missing values


#PRINT THE COLUMNS
# print("\nColumns:", fraud_detection_data.columns.tolist())


# PRINT DATA TYPES
# print("\nData Types:\n", fraud_detection_data.dtypes)


# TRANSACTION TYPE DISTRIBUTION
# print(fraud_detection_data['TransactionType'].value_counts())


# CHECK FOR DUPLICATES BEFORE REMOVAL
# print("Duplicates before:", fraud_detection_data.duplicated().sum()) #NO DUPLICATES

 
#DROP IRRELEVANT COLUMNS AND PRINT
# fraud_detection_data = fraud_detection_data.drop(columns=["TransactionID", "AccountID", "DeviceID", "IP Address", "MerchantID"])
# fraud_detection_data.head()
# print("Shape after cleanup:", fraud_detection_data.shape)
# print(fraud_detection_data.dtypes)


# print(fraud_detection_data) #after dropping, the number of column is 11


#E.D.A

# FraudFlag column with 0 = non-fraud, 1 = fraud.

# Example rules for marking suspicious (fraudulent) transactions
fraud_detection_data['FraudFlag'] = 0  # default = non-fraud

# Rule 1: Very high transaction amount (> 500)
fraud_detection_data.loc[fraud_detection_data['TransactionAmount'] > 500, 'FraudFlag'] = 1

# Rule 2: Too many login attempts (> 3)
fraud_detection_data.loc[fraud_detection_data['LoginAttempts'] > 3, 'FraudFlag'] = 1

# Rule 3: Very long transaction duration (> 200 sec)
fraud_detection_data.loc[fraud_detection_data['TransactionDuration'] > 200, 'FraudFlag'] = 1

print(fraud_detection_data['FraudFlag'].value_counts())



# # Initialize FraudFlag to 0 (non-fraud)
# fraud_detection_data['FraudFlag'] = 0  

# # Consider only Debit transactions
# debit_data = fraud_detection_data['TransactionType'] == 'Debit'

# # Rule 1: Very high transaction amount (> 500) for Debit only
# fraud_detection_data.loc[debit_data & (fraud_detection_data['TransactionAmount'] > 500), 'FraudFlag'] = 1

# # Rule 2: Too many login attempts (> 3) for Debit only
# fraud_detection_data.loc[debit_data & (fraud_detection_data['LoginAttempts'] > 3), 'FraudFlag'] = 1

# # Rule 3: Very long transaction duration (> 200 sec) for Debit only
# fraud_detection_data.loc[debit_data & (fraud_detection_data['TransactionDuration'] > 200), 'FraudFlag'] = 1

# print(fraud_detection_data['FraudFlag'].value_counts())



# 1. Distribution of key numeric features (histograms)
numeric_features = ['TransactionAmount', 'CustomerAge', 'TransactionDuration', 'LoginAttempts', 'AccountBalance']

fraud_detection_data[numeric_features].hist(figsize=(12,8), bins=30)
plt.suptitle("Distribution of Numeric Features", fontsize=14)
plt.show()


# 2. Compare Fraud vs Non-Fraud (boxplots)
for col in numeric_features:
    plt.figure(figsize=(6,4))
    sns.boxplot(data=fraud_detection_data, x='FraudFlag', y=col)
    plt.title(f"{col} by Fraud vs Non-Fraud")
    plt.show()


# 3. Correlation heatmap
plt.figure(figsize=(10,6))
corr = fraud_detection_data[numeric_features + ['FraudFlag']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


# 4. Outlier detection (using boxplots)
for col in numeric_features:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=fraud_detection_data[col])
    plt.title(f"Outliers in {col}")
    plt.show()

# (Optional) Detect outliers numerically with Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(fraud_detection_data[numeric_features]))
outliers = (z_scores > 3).sum()
print("Number of outliers per feature:\n", dict(zip(numeric_features, outliers)))






# finding the highest and lowest transaction amounts
highest_amount = fraud_detection_data['TransactionAmount'].max()
lowest_amount = fraud_detection_data['TransactionAmount'].min()

print("Highest Transaction Amount:", highest_amount)
print("Lowest Transaction Amount:", lowest_amount)