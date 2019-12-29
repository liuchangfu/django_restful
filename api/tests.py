from django.test import TestCase
import os
import yaml
import pymysql

# Create your tests here.

# 打开数据库连接
db = pymysql.connect('localhost', 'root', 'root', 'django_restful')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api', 'test_project', 'data', 'datas.yaml')
with (open(path, 'r', encoding='utf8')) as f:
    datas = yaml.load(f, Loader=yaml.FullLoader)
print(datas)
data = datas['data1']
print(data)
for i in range(len(datas['data1'])):
    tabel_name = datas['database1']
    id = datas['data1'][i]['id']
    usrname = datas['data1'][i]['username']
    email = datas['data1'][i]['email']
    groups = datas['data1'][i]['groups']
    sql = f"""INSERT INTO {tabel_name}(id,username, email, groups) VALUES ('{id}', '{usrname}', '{email}', '{groups}')"""
    print(sql)

for i in range(len(datas['data1'])):
    tabel_name = datas['database2']
    id = datas['data2'][i]['id']
    name = datas['data2'][i]['name']
    sql = f"""INSERT INTO {tabel_name}(id,name) VALUES ('{id}', '{name}')"""
    print(sql)

# print(datas['data1'][1]['id'])
# print(datas['data1'][1]['username'])
# print(datas['data1'][1]['email'])
# print(datas['data1'][1]['groups'])

# print(datas['database2'])
# print(datas['data2'])
# print(datas['data2'][0])
# print(datas['data2'][1])
