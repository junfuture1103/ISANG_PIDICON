import pandas as pd
import math

class Birthday:
    def __init__(self, month, day):
        self.month = month
        self.day = day
        
file_path = "./datasets/"
file_name = "data_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)
#data.shape => rows x cols
# print(read_data.shape)
# print(read_data)

signin_date_list = read_data.loc[:, '회원가입일']
signin_year_list = []

now_year = 2021

signin_year_list=[]
signin_year_list_2 = []
signin_year_list_4 = []
signin_year_list_6 = []

for signin_date in signin_date_list:
    # print(signin_date)
    year = int(signin_date.split('-')[0][:])
    # print(year)
    
    signin_year_list.append(year)
    year_gap = now_year - year
    
    interval = 2
    signin_year_list_2.append(str(math.ceil(year_gap / interval)*interval)+"년 이하")
    
    interval = 4
    signin_year_list_4.append(str(math.ceil(year_gap / interval)*interval)+"년 이하")
    
    interval = 8
    signin_year_list_6.append(str(math.ceil(year_gap / interval)*interval)+"년 이하")

level0 = signin_date_list
level1 = pd.DataFrame(signin_year_list)
level2 = pd.DataFrame(signin_year_list_2)
level3 = pd.DataFrame(signin_year_list_4)
level4 = pd.DataFrame(signin_year_list_6)

# level2_3
# level2 = pd.DataFrame(BIG_MIDDLE_address)

# level3
# 그냥 year만

# Address_Hierarchy = pd.concat([level1], axis = 1)
Address_Hierarchy = pd.concat([level0, level1, level2, level3, level4], axis = 1)
# Address_Hierarchy = pd.concat([level0, level1], axis = 1)
# print(Address_Hierarchy)

Address_Hierarchy.to_csv('hierarchys/sign_in_hierarchy.csv', header = None, encoding = 'ANSI', index = False)
print('Done Address Process')

# apply datasets
preprocessed_data = read_data
print(len(signin_year_list))

preprocessed_data['회원가입일'] = signin_year_list
preprocessed_data.to_csv('signin_datasets.csv')