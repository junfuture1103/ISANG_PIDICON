import pandas as pd

file_path = "./datasets"
file_name = "isang_test.csv"

file_path += file_name

df = pd.read_csv(file_path)