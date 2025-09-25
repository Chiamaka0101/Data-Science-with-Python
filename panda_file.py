import pandas as pd

data = {
  "Name": ["John", "Korede", "Daniel"],
  "Age": [25, 30, 28],
  "City": ["Rivers", "Imo", "Lagos"]
}

df = pd.DataFrame(data)

# print(df)
# print(df["Name"]) #print the names
# print(df.info)
# print(df.head())
# print(df.tail())
# print(df.shape) 



examdata = {
  "Name": ["Mike", "David", "Daniel", "Korede", "Stephane", "Frank"],
  "Study Hours": ["5", "3", "8", "2", "7", "4"],
  "Sleep Hours": ["7", "6", "6", "5", "8", "7"],
  "Score": ["80", "60", "92", "55", "88", "72"]
}

# Create a DataFrame from the dictionary
ed = pd.DataFrame(examdata)

# Display the full DataFrame
# print(ed)

# Print summary info: column names, non-null counts, data types, memory usage
# print(ed.info())

# Print descriptive statistics (count, mean, std, min, max, etc.)
# print(ed.describe())



