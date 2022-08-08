import pandas as pd

"""
Olyan, mint egy adatbázis tábla

a DataFrame az Series-ekből áll
"""
my_dict = {
    'forint': [400, 410, 408, 406],
    'euro': [1, 1, 1, 1],
    'dollar': [1, 1.1, 1.2, 1]
}

indexes = ['day1', 'day2', 'day3', 'day4']

df = pd.DataFrame(my_dict, index=indexes)


# print(df.loc[['day1', 'day3']])
#print(df)

#print(df['forint']['day3'])
#print(type(df['forint']))

# print(df[['euro', 'dollar']].loc['day1'])


####################


my_dict = {
    'forint': [400, None, 408, 406],
    'euro': [1, 1, 1, 1],
    'dollar': [1, 1.1, 1.2, 1],
    'day': ['mon', 'tue', 'wed', 'thu']
}

my_dict2 = {
    'forint': [260, 265, None, 310],
    'euro2': [1, 1, 1, 1],
    'dollar': [0.9, 0.99, 1.0, 1.1],
    'day': ['mon', 'tue', 'wed', 'thu']
}

df1 = pd.DataFrame(my_dict)
df2 = pd.DataFrame(my_dict2, index=['day1', 'day2', 'day3', 'day4'])

# dataframek egyesítése
#df1.rename(columns={'euro': 'euro2'}, inplace=True)

#print(df1)

df = pd.concat([df1, df2], join='inner')

print(df)
# print(df.loc[[0, 1]])


df = pd.merge(df1, df2, how='inner', left_on = ['day'], right_on = [ 'day'])

#df.dropna(inplace=True)

print(df[['forint_x', 'forint_y']])