import os
##相对路径
# class RelativePaths:
#     def __init__(self):
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
datas_path=os.path.join(base_path,r'datas\test.xlsx')
conf_path=os.path.join(base_path,'conf')
logs_path=os.path.join(base_path,'logs')
reports_path=os.path.join(base_path,'reports')

# print(base_path)
# print(datas_path)

if __name__ == '__main__':
    print(base_path)