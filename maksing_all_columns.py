import pandas as pd

def drop_column():
    file_path = "./datasets/"
    file_name = "isang_utf8.csv"

    file_path += file_name

    data = pd.read_csv(file_path)

    remove_col = '핸드폰번호'
    # 삭제처리할 열 확인
    # df = data.drop(['주소', '핸드폰번호'], axis=1)
    df = data.drop([remove_col], axis=1)

    # for make result document
    masking_col = ['*'] * df.shape[0]
    data[remove_col] = masking_col
    
    # for ARX
    df.to_csv('datasets/for_arx.csv', header = None, encoding = 'ANSI', index = False)
    # for result document    
    data.to_csv('datasets/drop_col.csv', encoding = 'UTF-8', index = False)
    
drop_column()