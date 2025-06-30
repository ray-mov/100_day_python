import pandas as pd
df = pd.read_json('data.json')
print(df.to_string())

# Tip: use to_string() to print the entire DataFrame.

# Dictionary as JSON
# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries.=======
# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:


df = pd.read_csv('data.csv')

print(df.head(10))
print(df.tail())
# Note: if the number of rows is not specified,
# the head() method will return the top 5 rows.
print(df.info())

# The info() method also tells us
# how many Non-Null values there are present in each column