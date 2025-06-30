import pandas as pd
#The corr() method calculates the relationship between each column in your data set.

#Note: The corr() method ignores "not numeric" columns.


df = pd.read_csv('data.csv')

print(df.corr())