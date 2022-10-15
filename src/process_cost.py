# 구매액, 누적구매액 등등 숫자 총계처리용(구간별 평균값 기반)
from cmath import nan
import pandas as pd
import outputs

pd.options.display.float_format = '{:.2f}'.format

file_path = "./datasets/"
file_name = "isang_utf8.csv"

file_path += file_name

data = pd.read_csv(file_path)

def make_statistic_hierarchy(inter_val):

    col = "일련번호" # 처리할 열
    interval = inter_val # 평균값 구할 구간

    this_data = data[col]
    outputs.create_txt(col)

    print(this_data.describe()) # 해당 열 분석

    max = this_data.max() # 해당 열의 최대값

    mean_list = [] # 구간별 평균값 저장할 리스트
    len_list = [] # 구간별 데이터 수 저장할 리스트

    print("\n===================== 평균 ======================")

    for x in range(0, max, interval):
        start = x
        end = x+interval
        
        # 해당 범위 내의 데이터들 추출
        temp = data[(this_data >= start) & (this_data < end)]
        temp_mean = temp[col].mean()
        
        mean_list.append(temp_mean)
        len_list.append(len(temp))
        
        print("{}이상 {}미만 : {}".format(start, end, temp_mean))
        
    print("==================================================\n")

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

    # make result .csv
    processed_data = data
    processed_data[col] = result_col_list

    print(result_col_list)

    processed_data.to_csv(col+".csv",encoding="utf-8")
    
    return result_col_list
    
level1_list = make_statistic_hierarchy(300000)
# level2_list = make_statistic_hierarchy(10000)
# level3_list = make_statistic_hierarchy(100000)

level1 = pd.DataFrame(level1_list)
# level2 = pd.DataFrame(level2_list)
# level3 = pd.DataFrame(level3_list)

# Address_Hierarchy = pd.concat([level1, level2, level3], axis = 1)
Address_Hierarchy = pd.concat([level1], axis = 1)
print(Address_Hierarchy)

Address_Hierarchy.to_csv('hierarchys/cost_hierarchy.csv', header = None, encoding = 'ANSI', index = False)

print('Done Cost Process')