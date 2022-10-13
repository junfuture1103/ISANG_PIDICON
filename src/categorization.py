import pandas as pd
import copy

file_path = "./datasets/"
file_name = "isang_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)

#data.shape => rows x cols
print(read_data.shape)
print(read_data)

def make_age_hierarchy(interval_num):
    age_list = read_data.loc[:, '나이']

    categorization_interval = interval_num
    initial_num = categorization_interval

    max = age_list.max() # 해당 열의 최대값
    len_list = []

    for category_num in range(0, max, categorization_interval):
        start = category_num
        end = category_num+categorization_interval
        print("category_num : ", category_num)
        # 해당 범위 내의 데이터들 추출
        age_list[(age_list >= start) & (age_list < end)] = category_num
        # temp = age_list[(age_list >= start) & (age_list < end)]
        # len_list.append(len(temp))
        
        print("{}이상 {}미만 : {}".format(start, end, category_num))
    
    print(age_list)
    
    return age_list
        
level1_list = make_age_hierarchy(5)
level2_list = make_age_hierarchy(10)
level3_list = make_age_hierarchy(30)

level1 = pd.DataFrame(level1_list)
level2 = pd.DataFrame(level2_list)
level3 = pd.DataFrame(level3_list)

Address_Hierarchy = pd.concat([level1, level2, level3], axis = 1)
Address_Hierarchy = pd.concat([level1], axis = 1)

print(Address_Hierarchy)

Address_Hierarchy.to_csv('hierarchys/age_hierarchy.csv', header = None, encoding = 'ANSI', index = False)

print('Done Address Process')