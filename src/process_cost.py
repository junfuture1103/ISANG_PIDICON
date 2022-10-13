# 구매액, 누적구매액 등등 숫자 총계처리용(구간별 평균값 기반)
from cmath import nan
import pandas as pd
import src.outputs as outputs

pd.options.display.float_format = '{:.2f}'.format

file_path = "./datasets/"
file_name = "isang_test_copy.csv"

file_path += file_name

data = pd.read_csv(file_path)

col = "구매액" # 처리할 열
interval = 300000 # 평균값 구할 구간

this_data = data[col]
outputs.create_txt(col)

print(this_data.describe()) # 해당 열 분석

max = this_data.max() # 해당 열의 최대값

mean_list = [] # 구간별 평균값 저장할 리스트
len_list = [] # 구간별 데이터 수 저장할 리스트

print("\n===========================================")
for x in range(0, max, interval):
    start = x
    end = x+interval
    temp = data[(this_data >= start) & (this_data < end)]

    temp_mean = temp[col].mean()
    mean_list.append(temp_mean)
    len_list.append(len(temp))
    print("{}이상 {}미만 : {}".format(start, end, temp_mean))
print("===========================================\n")

print(mean_list)
print(len_list)

for i in range(len(mean_list)):
    data.loc[data[col]//interval == i, col] = mean_list[i]
    if (mean_list[i] == nan):
        mean_list[i] = 0

result_col_list = []
col_list = this_data.values
for col_value in col_list:
    col_value = float(col_value)
    index = int(col_value//interval)
    col_value = int(mean_list[index])
    result_col_list.append(col_value)

processed_data = data
processed_data[col] = result_col_list

processed_data.to_csv(col+".csv",encoding="utf-8")