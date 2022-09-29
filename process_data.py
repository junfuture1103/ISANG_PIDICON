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
'''

print(data['주소'].value_counts()) # Large_Addr + Middle_addr + Small_Addr
data.info() # 컬럼의 종류와 각 데이터 개수, NaN의 개수 확인 수량만 50만개가 아닌 49만개로 뭔가 다름을 알 수 있음.

data.describe() # 아래 목록을 보여줌, 경계값을 대체하기 위한 평균값이나 25%,50%,75% 구하기 수월함.
#count: not null인 데이터 건수
#mean: 전체 데이터의 평균값
#std: 표준편차
#min: 최솟값
#max: 최대값
#25%: 25 percentile 값
#50%: 50 percentile 값
#75%: 75 percentile 값


data1 = pd.read_csv(file_path) # Large_Addr + Middle addr # 중간 주소까지 전처리 이때 경기와 경기도 둘로 나누어지므로 전처리 필요

for i in range(0,500000):
    temp=data1.loc[i,'주소']
    temp1=temp.split(' ')[0]
    temp2=temp.split(' ')[1]
    if len(temp1)==3:
        temp1=temp1[:-1]
    temp=temp1+' '+temp2
    data1.loc[i,'주소']=temp


data2 = pd.read_csv(file_path) # Large_Addr 즉 시 기준으로 전처리 단 이때 경기는 경기와 경기도 둘로 나누어지므로 전처리 추가로 필요
for i in range(0,500000):
    temp=data2.loc[i,'주소']
    temp=temp.split(' ')[0]
    if len(temp)==3:
        temp=temp[:-1]
    data2.loc[i,'주소']=temp

전처리 후의 결과 값은 너무 길어서 따로 파일로 작성하여 깃허브에 올려놓음.




'''
