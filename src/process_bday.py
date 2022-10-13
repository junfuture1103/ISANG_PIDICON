import pandas as pd

class Birthday:
    def __init__(self, month, day):
        self.month = month
        self.day = day


file_path = "./datasets/"
file_name = "isang_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)

bday = read_data.loc[:, '생일']

bday_list = []

for data in bday:
    tmp = Birthday(int(data.split(' ')[0][:-1]), int(data.split(' ')[1][:-1]))
    bday_list.append(tmp)

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

    print('Done Process')

def get_birthday_count():
    tmp_list = []

    index = 0
    index_list = []

    month_count = [0 for i in range(0,12)] # 생일 월별 데이터 수 저장할 리스트

    for data in bday_list:
        month_count[data.month-1]+=1

    # 각 월 별 생일인 사람의 데이터가 몇 개인지 count해서 출력
    print(month_count)

