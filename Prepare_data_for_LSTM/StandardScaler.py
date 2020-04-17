from sklearn.preprocessing import StandardScaler
import math
import pandas as pd  

# define series
data = [1.0, 5.5, 9.0, 2.6, 8.8, 3.0, 4.1, 7.9, 6.3]
series = pd.Series(data)
print(series)

# prepare data for normalization
values = series.values
values = values.reshape((len(values), 1))

# train the normalization
scaler = StandardScaler()
scaler = scaler.fit(values)
print("Mean: {}, StandardDeviation".\
        format(scaler.mean_, math.sqrt(scaler.var_)))

# normalize the dataset and print
standardized = scaler.transform(values)
print(standardized)

# inversed transform and print
inversed = scaler.inverse_transform(standardized)
print(inversed)