import pandas as pd 

# define the sequence
df = pd.DataFrame()
df['t'] = [x for x in range(10)]
#print(df)

# shift forward
# df['t-1'] = df['t'].shift(1)
# print(df)

# shift backward 
df['t+1'] = df['t'].shift(-1)
print(df)