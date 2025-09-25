import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = pd.read_csv("titanic.csv") #make sure the csv file is in the root folder
# print(titanic_data.head()) #shows the first few rows (default 5).

# print(titanic_data.tail())  #shows the last few rows (default 5).


#DATA CLEANING


#to handle missing values
print(titanic_data.isnull().sum()) 


#to fill in missing values. Take the median of the Age column. Fill missing values (NaN) with that median. Apply it in place
# titanic_data["Age"].fillna(titanic_data["Age"].median(), inplace=True)
titanic_data["Age"] = titanic_data["Age"].fillna(titanic_data["Age"].median())



# drop the Cabin column (notice capital 'C')
titanic_data.drop("Cabin", axis=1, inplace=True)

# fill Embarked with the most common value (mode)
titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0], inplace=True)

# change gender to 0 and 1
titanic_data["Sex"] = titanic_data["Sex"].map({"male": 0, "female": 1})

# drop irrelevant columns
titanic_data.drop(["PassengerId", "Ticket", "Name"], axis=1, inplace=True)

#Count of survivors
# print("\n Value count for survived", titanic_data["Survived"].value_counts())

# print("\n Value count for sex", titanic_data["Sex"].value_counts())


# print(titanic_data)


# DATA VISUALIZATION
sns.countplot(x='Survived', data=titanic_data)

plt.title("Survival count(0=DIED, 1=Survived)")
plt.show()

sns.countplot(x='Survived', hue='Survived', data=titanic_data)
plt.title("Survival by Gender")
plt.show()

sns.histplot(titanic_data['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()


sns.boxplot(x='Pclass', y='Age', data=titanic_data)
plt.title("Age Distribution by Passenger")
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(titanic_data.corr(), annot=True, cmap='coolwarm', fmt='2.f')
plt.title("Correction Heatmap")
plt.show()
