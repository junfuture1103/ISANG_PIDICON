import pandas as pd
import remove_outlier

class Address:
    def __init__(self, large, middle, small):
        self.Large_Addr = large
        self.Middle_Addr = middle
        self.Small_Addr = small

    # def set_addr(self, large, middle, small):
    #     self.Large_Addr = large
    #     self.Middle_Addr = middle
    #     self.Small_Addr = small
    #     return
    
    # def print_addr(self):
    #     print(self.Large_Addr , end = '')
    #     print(self.Middle_Addr , end = '')
    #     print(self.Small_Addr , end = '')


file_path = "./datasets/"
file_name = "isang_test.csv"

file_path += file_name

data = pd.read_csv(file_path)

#data.shape => rows x cols
print(data.shape)
print(data)

#column 나누기 loc[행, 열]
# samples = data.loc[:, '이름' : '성별']
addr = data.loc[:, '주소']

addr_list = []

for ad in addr:
    # print(ad.split(' ')[0], ad.split(' ')[1],ad.split(' ')[2])
    tmp = Address(ad.split(' ')[0], ad.split(' ')[1],ad.split(' ')[2])
    addr_list.append(tmp)

tmp_list = []

index = 0
index_list = []

for ad in addr_list:
    # print(ad.Large_Addr, ad.Middle_Addr, ad.Small_Addr)
    if (ad.Large_Addr == '서울'):
        index_list.append(index)
    index += 1

seoul_data = data.loc[index_list]

print(seoul_data)
#print(data['주소'].value_counts())
