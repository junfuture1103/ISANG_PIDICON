import pandas as pd

class Birthday:
    def __init__(self, month, day):
        self.month = month
        self.day = day


file_path = "./datasets/"
file_name = "isang_test.csv"

file_path += file_name

data = pd.read_csv(file_path)

bday = data.loc[:, '생일']

bday_list = []

for data in bday:
    tmp = Birthday(int(data.split(' ')[0][:-1]), int(data.split(' ')[1][:-1]))
    bday_list.append(tmp)

tmp_list = []

index = 0
index_list = []

month_count = [0 for i in range(0,12)] # 생일 월별 데이터 수 저장할 리스트

for data in bday_list:
    month_count[data.month-1]+=1

# 각 월 별 생일인 사람의 데이터가 몇 개인지 count해서 출력
print(month_count)

