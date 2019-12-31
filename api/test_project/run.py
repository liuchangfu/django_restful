# _*_ coding:utf-8 _*_
import os
import datetime
import unittest
from loguru import logger
from BSTestRunner import BSTestRunner
from mysql_action import DB

# run.py所有的当前目录
curdir = os.path.abspath(os.curdir)
logger.info(f'当前目录为：{curdir}')

log = curdir + '//log' + '//run.txt'
logger.info(f'log的目录为:{log}')
logger.add(log, encoding='utf-8')

db = DB()
db.init_data()

# 测试用例文件夹
# testDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_project', 'testDir')

testDir = curdir + '//testDir'
logger.info(f'testDir目录为：{testDir}')

# 测试报告文件夹
# report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_project', 'report/')
report = curdir + '//report//'
logger.info(f'report目录为：{report}')

# 加载测试用例
# discover = unittest.defaultTestLoader.discover(testDir, pattern='test*.py')
discover = unittest.TestLoader().discover("testDir")

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# 测试报告名字
report_name = report + now + '_test_report.html'
logger.info(report_name)

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Api Test Report', description='Django restful Api test report')
    logger.info('Api Test.......')
    runner.run(discover)
