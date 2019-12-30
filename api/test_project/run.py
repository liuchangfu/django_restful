# _*_ coding:utf-8 _*_
import os
import sys
dir = os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(dir)
print(dir)
print(sys.path)
import datetime
import unittest
from loguru import logger
from api.test_project.BSTestRunner import BSTestRunner
from api.test_project.mysql_action import DB

log = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_project', 'log', 'run.txt')
logger.add(log, encoding='utf-8')

db = DB()
db.init_data()

# 测试用例文件夹
testDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_project', 'testDir')
logger.info(testDir)

# 测试报告文件夹
report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_project', 'report')
logger.info(report)

# 加载测试用例
discover = unittest.defaultTestLoader.discover(testDir, pattern='test*.py')

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# 测试报告名字
report_name = report + '/' + now + '_test_report.html'
logger.info(report_name)

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Api Test Report', description='Django restful Api test report')
    logger.info('Api Test.......')
    runner.run(discover)
