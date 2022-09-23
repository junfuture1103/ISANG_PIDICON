import pandas as pd
import remove_outlier

file_path = "./datasets/"
file_name = "isang_test.csv"

file_path += file_name

data = pd.read_csv(file_path)

#data.shape => rows x cols
print(data.shape)
print(data)

#column 나누기 loc[행, 열]
samples = data.loc[:, '이름' : '성별']
sample = data.loc[:, '구매액']

#이상치 제거
sample = remove_outlier.remove_out(sample)

print(sample)
#test