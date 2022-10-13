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
address = data.loc[:, '주소']

print(address)

addrs_list = []
addr_dict = {"Big_Address":[], "Middle_Address":[], "Small_Address":[]}

for ad in address:
    # print(ad.split(' ')[0], ad.split(' ')[1],ad.split(' ')[2])
    addr_dict["Big_Address"].append(ad.split(' ')[0])
    addr_dict["Middle_Address"].append(ad.split(' ')[1])
    addr_dict["Small_Address"].append(ad.split(' ')[2])

address_df = pd.DataFrame(addr_dict)

# 고유한 큰주소들 알아내기
unique_big_addr = address_df['Big_Address'].unique()
unique_middle_addr = address_df['Middle_Address'].unique()
unique_small_addr = address_df['Small_Address'].unique()

print(unique_big_addr)
print(unique_middle_addr)
print(unique_small_addr)

Big_Addresses = address_df['Big_Address']
Middle_Addresses = address_df[['Big_Address', 'Middle_Address']]
Small_Addresses = address_df

Big_Address_count = Big_Addresses.value_counts()
Middle_Address_count = Middle_Addresses.value_counts()
Small_Address_count = Small_Addresses.value_counts()

print(Big_Address_count)
print(Middle_Address_count)
print(Small_Address_count)

Big_Address_count.to_csv('대주소_count.csv')
Middle_Address_count.to_csv('대중주소_count.csv')
Small_Address_count.to_csv('대중소주소_count.csv')

new_address = []

de_identification_level = int(input("대(1) / 대중(2) / 대중소(3) level을 골라주세요 : "))

if(de_identification_level == 1 or de_identification_level == 2):
    for ad in address:
        # print(ad.split(' ')[0], ad.split(' ')[1],ad.split(' ')[2])
        if(de_identification_level == 1):
            tmp = ad.split(' ')[0]
        elif(de_identification_level == 2):
            tmp = ad.split(' ')[0] + ' ' +  ad.split(' ')[1]
        new_address.append(tmp)
else:
    new_address = address
    
preprocessed_data = data
preprocessed_data['주소'] = new_address

print(data)
print(preprocessed_data)

preprocessed_data.to_csv('preprocessed_data.csv')
print('Done Process')

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
