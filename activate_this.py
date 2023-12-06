import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Import dữ liệu vô với biến là df
df = pd.read_csv('ecommerce_customer_data_large.csv')

# Coi mấy dòng đầu
df.head()

# Thống kê mô tả cơ bản: mean, std, min, max, tứ phân vị
df.describe()

# Tóm tắt các trường dữ liệu còn lại
df.describe(include='O')

# Tìm dữ liệu bị thiếu --> print ra số dữ liệu không bị rỗng
df.info()

# Xóa dữ liệu bị lặp (hàng)
df.drop_duplicates(inplace=True)

# Check bao nhiêu thông tin bị thiếu --> cái return (trả lại) là thiếu nhiều nhất, mà cái này mình không có sử dụng
missing_values = df.isnull().sum()
# print("Missing Values:", missing_values)

# Điền vô giá trị = 0
default_return_value = 0
df['Returns'].fillna(default_return_value, inplace=True)
# print(df.isnull().sum())
