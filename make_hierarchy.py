import os
import src
from src import hierarchy

if __name__ == '__main__':
    print(os.path.realpath(__file__))
    
    # 주소 전처리
    hierarchy.make_address_hierarchy()
    
    # 생일 전처리
    hierarchy.make_birthday_hierarchy()
    hierarchy.get_birthday_count()