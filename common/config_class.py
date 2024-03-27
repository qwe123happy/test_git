import configparser
from common import constants
import os
config=configparser.ConfigParser()
config.read(os.path.join(constants.conf_path,'updata_data.conf'),encoding='utf-8')
data=config.get('switch','button')

if data =='uat':
    config.read(os.path.join(constants.conf_path,'uat_environment.conf'), encoding='utf-8')
    url = config.get('data_url', 'url')
    host=config.get('connect_data','host')
    user=config.get('connect_data','user')
    password=config.get('connect_data','password')
    port=config.getint('connect_data','port')
    database=config.get('connect_data','database')
    # print(url)
    # print(host)
    # print(user)
    # print(password)
    # print(type(port))
    # print(database)
elif data == 'db':
    config.read(os.path.join(constants.conf_path,'db_environment.conf'),encoding='utf-8')
    url =config.get('data_url','url')
    host = config.get('connect_data', 'host')
    user = config.get('connect_data', 'user')
    password = config.get('connect_data', 'password')
    port = eval(config.get('connect_data', 'port'))
    database = config.get('connect_data', 'database')
else:
    print('没有这种环境配置，检查是否拼写错误')

