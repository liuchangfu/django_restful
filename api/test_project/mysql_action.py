# _*_ coding:utf-8 _*_
from pymysql import connect
import yaml
from loguru import logger
import os


class DB(object):

    def __init__(self):
        """连接数据库"""
        logger.info('连接数据库.......')
        self.conn = connect(host='127.0.0.1', user='root', password='root', db='django_restful')
        self.cursor = self.conn.cursor()
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_project', 'data', 'datas.yaml')
        with (open(path, 'r', encoding='utf8')) as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def run_api_uesr(self):
        self.clear(self.data['database1'])
        logger.info('正在插入api_user表数据........')
        global sql
        for i in range(len(self.data['data1'])):
            tabel_name = self.data['database1']
            id = self.data['data1'][i]['id']
            username = self.data['data1'][i]['username']
            email = self.data['data1'][i]['email']
            groups = self.data['data1'][i]['groups']
            sql = f"""INSERT INTO {tabel_name}(id,username, email, `groups`) VALUES ({id}, '{username}', '{email}', '{groups}')"""
            self.insert(sql)

    def run_api_group(self):
        self.clear(self.data['database2'])
        logger.info('正在插入api_group表数据........')
        global sql
        for i in range(len(self.data['data1'])):
            tabel_name = self.data['database2']
            id = self.data['data2'][i]['id']
            name = self.data['data2'][i]['name']
            sql = f"""INSERT INTO {tabel_name}(id,name) VALUES ({id}, '{name}')"""
            self.clear(self.data['database2'])
            self.insert(sql)

    def clear(self, table_name):
        """清除表中数据"""
        clear_sql = 'truncate ' + table_name + ';'
        self.cursor.execute('set foreign_key_checks=0;')
        self.cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self, sql):
        """插入数据"""


        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            db.conn.commit()
        except:
            # 如果发生错误则回滚
            db.conn.rollback()

    def close(self):
        """关闭数据库连接"""
        logger.info('关闭数据库.......')
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    db.run_api_group()
    db.run_api_uesr()
    db.close()
