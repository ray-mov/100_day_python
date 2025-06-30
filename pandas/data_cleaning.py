import pandas as pd


# Pandas - Cleaning Empty Cells

# remove rows that contain empty cells.

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:

df.dropna(inplace = True)

print(df.to_string())

df.fillna(130, inplace = True)
df.fillna({"Calories": 130}, inplace=True) # specific column

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)



# Cleaning Data of Wrong Format

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
#Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

#Fixing Wrong Data

# Set "Duration" = 45 in row 7:

df.loc[7, 'Duration'] = 45
# If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

#Delete rows where "Duration" is higher than 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# Removing Duplicates
# Returns True for every row that is a duplicate, otherwise False:

print(df.duplicated())
df.drop_duplicates(inplace = True)
