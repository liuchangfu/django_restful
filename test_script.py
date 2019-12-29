import pymysql

# 打开数据库连接
db = pymysql.connect('localhost', 'root', 'root', 'django_restful')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
# cursor.execute('SELECT VERSION()')
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print(f'Database version:{data}')
# # 关闭数据库连接
# db.close()

# sql = """
# CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )
# """
# cursor.execute(sql)
# db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
