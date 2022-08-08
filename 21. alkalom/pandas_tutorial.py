import pandas as pd

"""
numpy - C-ben írt, adatstruktúrák 

Series
DataFrame
Panel - x három dimenziós tömb

"""


# Series - egy oszlop az excelben, egy oszlop egy adatbázis táblában

# index - label - hashelhető adatnak kell lennie


s = pd.Series([1, 2, '3', 4, 5, 6], index = ['a','b','c','d','e', 'f'])

# object - string

#print(s[4])
#print(s)

# print(s.dtype)

# print(s.head(3))
# print(s.tail(2))

# print(s.index)

#print(s[::-1])

my_dict = {'day1': 400, 'day2': 410, 'day3': 408, 'day4': 404, 'day5': 408}

s2 = pd.Series(my_dict)

s3 = pd.Series(my_dict, index=['day1', 'day2'])



print(s3['day2'])

df = pd.DataFrame({'huf_10':s2, 'huf_11': s3})

print(df)











