import pandas as pd

sheet2=pd.read_excel('./datasets/01_(데이터셋) PIDICON_2022_예선경연용 데이터셋.xlsx',engine='openpyxl',sheet_name=1)# 2번째 시트

file_path = "./datasets/"
file_name = "final_8481_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)
df = read_data

df_prd = sheet2[['소분류','삼품이름']]

print(df["2021 하반기 최고가 구매상품"].count())

level1 = df_prd["삼품이름"]
level2 = df_prd["소분류"]

Address_Hierarchy = pd.concat([level1, level2], axis = 1)
print(Address_Hierarchy)

Address_Hierarchy.to_csv('./hierarchys/item.csv', header = None, encoding = 'ANSI', index = False)