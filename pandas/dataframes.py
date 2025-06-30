# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns.
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar  = pd.DataFrame(data)
print(myvar)
print(myvar.loc[0])
#The loc attribute to return one or more specified row(s)
print(myvar.loc[[0, 1]])

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])

df2 = pd.read_csv('data.csv')
print(df2)
print(df2.to_string())
print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999
# check your system's maximum rows with the pd.options.display.max_rows statement.
