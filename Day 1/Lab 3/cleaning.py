import pandas as pd
df=pd.read_csv("D:\\mini project\\train.csv")
print(df.info())
print()
print(df.isnull().sum())
print()
print(df['Order Date'])
print()
df = df.drop(columns=['Postal Code'])
print(df.isnull().sum())
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
print("Duplicate rows:", df.duplicated().sum())
df['Order_Year'] = df['Order Date'].dt.year
df['Order_Month'] = df['Order Date'].dt.month
df['Order_Weekday'] = df['Order Date'].dt.day
print(df.info())
print(df.select_dtypes(include='object').columns)
df.to_csv('final_sales_dataset.csv', index=False)

