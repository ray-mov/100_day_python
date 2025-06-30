import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pandas.DataFrame(mydataset)
#
# print(myvar)
# print(pandas.__version__)

#series =============================================

# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

a = [1,4,5]

myvar  = pd.Series(a, index = ['x','y','z'])
# With the index argument, you can name your own labels.

print(myvar)
print(myvar['y'])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2 = pd.Series(calories)
print(myvar2)