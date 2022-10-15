import pandas as pd
import copy

file_path = "./datasets/"
file_name = "data_utf8.csv"

file_path += file_name

read_data = pd.read_csv(file_path)

#data.shape => rows x cols
print(read_data.shape)
print(read_data)

job_list = read_data.loc[:, '직업분류코드']

job_level1_list=[]
job_level2_list=[]
job_level3_list=[]
job_level4_list=[]

for job_code in job_list:
    if(job_code == 0):
        job_level1_list.append(0)
        job_level2_list.append(0)
        job_level3_list.append(0)
        job_level4_list.append(0)
    else:
        job_code_str = str(job_code)
        job_level1_list.append(job_code_str[:-1])
        job_level2_list.append(job_code_str[:-2])
        job_level3_list.append(job_code_str[:-3])
        job_level4_list.append(job_code_str[:-4])

level0 = job_list
level1 = pd.DataFrame(job_level1_list)
level2 = pd.DataFrame(job_level2_list)
level3 = pd.DataFrame(job_level3_list)
level4 = pd.DataFrame(job_level4_list)

# Address_Hierarchy = pd.concat([level1], axis = 1)
Address_Hierarchy = pd.concat([level0, level1, level2, level3, level4], axis = 1)
# print(Address_Hierarchy)

Address_Hierarchy.to_csv('hierarchys/job_code_hierarchy.csv', header = None, encoding = 'ANSI', index = False)
print('Done Address Process')

# apply datasets
preprocessed_data = read_data

preprocessed_data['직업분류코드'] = level1
preprocessed_data.to_csv('job_code_datasets.csv')