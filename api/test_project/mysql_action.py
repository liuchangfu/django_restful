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

    def clear(self, table_name):
        """清除表中数据"""
        logger.info('清除数据......')
        clear_sql = 'truncate ' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('set foreign_key_checks=0;')
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        """插入数据"""
        logger.info('插入数据........')

        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
            key = ','.join(table_data.keys())
            value = ','.join(table_data.values())
            logger.info(f'1----{key}')
            logger.info(f'2----{value}')
            insert_sql = 'insert into ' + table_name + "(" + key + ")" + " values" + "(" + value + ")"
            logger.info(f"{insert_sql}")
            with self.conn.cursor() as cursor:
                cursor.execute(insert_sql)
            self.conn.commit()

    def close(self):
        """关闭数据库连接"""
        logger.info('关闭数据库.......')
        self.conn.close()

    def init_data(self, datas):
        """初始化数据"""
        logger.info('初始化数据......')
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
            self.close()


if __name__ == '__main__':
    db = DB()
    path = os.path.join(os.path.dirname(__file__), 'data', 'datas.yaml')
    with (open(path, 'r', encoding='utf8')) as f:
        datas = yaml.load(f, Loader=yaml.FullLoader)
    print(datas)
    # db.init_data(datas)
