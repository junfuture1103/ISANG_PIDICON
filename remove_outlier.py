import pandas as pd

def remove_out(dataframe):
    dff = dataframe
    print(dff, type(dff))

    MAX = 100000000
    MIN = 3000
    
    #이상치 제거 후 남은 행만 담음
    dff = dff[(dff <= MAX) & (dff >=MIN)]
    dff = dff.reset_index(drop=True)

    return dff