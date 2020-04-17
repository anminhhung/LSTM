from pandas import Series
from sklearn.preprocessing import MinMaxScaler

# khởi tạo series
data = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
series = Series(data)
print(series)

# Chuẩn bị dữ liệu cho quá trình normalize
values = series.values
values = values.reshape((len(values), 1))

# thực hiện huấn luyện và normalize dataset
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print("Minimum: {}, Maximum: {}".format(scaler.data_min_, scaler.data_max_))

normalized = scaler.transform(values)
print(normalized)

# inverse transform and print
inversed = scaler.inverse_transform(normalized)
print(inversed)
