import pandas as pd

class Address:
    def __init__(self, large, middle, small):
        self.Large_Addr = large
        self.Middle_Addr = middle
        self.Small_Addr = small

def make_address_hierarchy():
    file_path = "./datasets/"
    file_name = "isang_utf8.csv"

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

    print('Done Process')

