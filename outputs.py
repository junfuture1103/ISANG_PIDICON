import sys

def create_txt(file_name):
    output_path = "./outputs/" # print될 값들은 해당 경로에 저장
    output_name = file_name+".txt"
    output_path += output_name
    sys.stdout = open(output_path,'w',encoding="UTF-8")


class JsonOutput():
    def __init__(self):
        self.key_list = []
        self.json_data = {}
    def add_key(self,key_name):
        self.key_list.append(key_name)
    
