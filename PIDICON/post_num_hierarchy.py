import pandas as pd
        
file_path = "./datasets/"
file_name = "data_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)
#data.shape => rows x cols
print(read_data.shape)
print(read_data)


#column 나누기 loc[행, 열]
# samples = data.loc[:, '이름' : '성별']
post_num_list = read_data.loc[:, '우편번호']

print(post_num_list)
level1_list = []
level2_list = []

for post_num in post_num_list:
    front_post_num = str(post_num)[0:3] 
    maked_post_num = front_post_num + "**"
    level1_list.append(maked_post_num)
    level2_list.append("*****")

level0 = post_num_list
level1 = pd.DataFrame(level1_list)
level2 = pd.DataFrame(level2_list)
# level3 = pd.DataFrame(level3_list)

# Address_Hierarchy = pd.concat([level1, level2, level3], axis = 1)
Address_Hierarchy = pd.concat([level0, level1, level2], axis = 1)

print(Address_Hierarchy)

Address_Hierarchy.to_csv('hierarchys/post_num_hierarchy.csv', header = None, encoding = 'ANSI', index = False)

print('Done post_num Process')