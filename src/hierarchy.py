import pandas as pd

class Birthday:
    def __init__(self, month, day):
        self.month = month
        self.day = day
        
file_path = "./datasets/"
file_name = "isang_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)
#data.shape => rows x cols
print(read_data.shape)
print(read_data)

bday = read_data.loc[:, '생일']
bday_list = []

for data in bday:
    tmp = Birthday(int(data.split(' ')[0][:-1]), int(data.split(' ')[1][:-1]))
    bday_list.append(tmp)

def make_address_hierarchy():
    #column 나누기 loc[행, 열]
    # samples = data.loc[:, '이름' : '성별']
    address = read_data.loc[:, '주소']
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

    BIG_address = []
    BIG_MIDDLE_address = []
    BIG_MIDDLE_SMALL_address = []
        
    for ad in address:
        # print(ad.split(' ')[0], ad.split(' ')[1],ad.split(' ')[2])
        tmp1 = ad.split(' ')[0]
        tmp2 = ad.split(' ')[0] + ' ' +  ad.split(' ')[1]

        BIG_address.append(tmp1)
        BIG_MIDDLE_address.append(tmp2)
        
    BIG_MIDDLE_SMALL_address = address

    level1 = pd.DataFrame(BIG_address)
    level2 = pd.DataFrame(BIG_MIDDLE_address)
    level3 = pd.DataFrame(BIG_MIDDLE_SMALL_address)

    Address_Hierarchy = pd.concat([level1, level2, level3], axis = 1)
    
    print(Address_Hierarchy)
    
    Address_Hierarchy.to_csv('hierarchys/address_hierarchy.csv', header = None, encoding = 'ANSI', index = False)

    print('Done Address Process')

def make_birthday_hierarchy():
    MONTH_DAY = bday
    MONTH = []
    MONTH_QUARTER = []
    
    for data in bday_list:
        MONTH.append(str(data.month)+'월')
        if (data.month <= 3):
            MONTH_QUARTER.append('1분기')
        elif (data.month <= 6):
            MONTH_QUARTER.append('2분기')
        elif (data.month <= 9):
            MONTH_QUARTER.append('3분기')
        elif (data.month <= 12):
            MONTH_QUARTER.append('4분기')

    level1 = pd.DataFrame(MONTH_DAY)
    level2 = pd.DataFrame(MONTH)
    level3 = pd.DataFrame(MONTH_QUARTER)

    Address_Hierarchy = pd.concat([level1, level2, level3], axis = 1)
    
    print(Address_Hierarchy)
    
    Address_Hierarchy.to_csv('hierarchys/birthday_hierarchy.csv', header = None, encoding = 'ANSI', index = False)

    print('Done Birthday Process')

def get_birthday_count():
    tmp_list = []

    index = 0
    index_list = []

    month_count = [0 for i in range(0,12)] # 생일 월별 데이터 수 저장할 리스트

    for data in bday_list:
        month_count[data.month-1]+=1

    # 각 월 별 생일인 사람의 데이터가 몇 개인지 count해서 출력
    print(month_count)

def make_age_hierarchy():
    age = read_data.loc[:, '나이']
    
    level1_interval = 5
    
    level1_list = []
    level2_list = []
    level3_list = []
    
    level1 = pd.DataFrame(level1_list)
    level2 = pd.DataFrame(level2_list)
    level3 = pd.DataFrame(level3_list)

    Address_Hierarchy = pd.concat([level1, level2, level3], axis = 1)
    
    print(Address_Hierarchy)
    
    Address_Hierarchy.to_csv('hierarchys/age_hierarchy.csv', header = None, encoding = 'ANSI', index = False)

    print('Done Birthday Process')