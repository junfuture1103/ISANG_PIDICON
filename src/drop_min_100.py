import pandas as pd

file_path = "./datasets/"
file_name = "arx1차_PIDICON_2022_utf8.csv"

file_path += file_name

df = pd.read_csv(file_path)

new_data = df[(df[' 2017년 총 구매액 ']>=1000000) & (df[' 2018년 총 구매액 ']>=1000000) & (df[' 2019년 총 구매액 ']>=1000000) & (df[' 2020년 총 구매액 ']>=1000000)]

print((df[' 2017년 총 구매액 ']>=1000000) & (df[' 2018년 총 구매액 ']>=1000000) & (df[' 2019년 총 구매액 ']>=1000000) & (df[' 2020년 총 구매액 ']>=1000000))
new_data = new_data.dropna(axis=0)

new_data.to_csv('8481_original.csv', header = None, encoding = 'ANSI', index = False)

print(len(new_data))

# print(good_idx.index)