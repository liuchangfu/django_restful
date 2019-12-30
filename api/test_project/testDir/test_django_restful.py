# _*_ coding:utf-8 _*_
import requests
import unittest
from api.test_project.mysql_action import DB
import yaml
from loguru import logger


class UserTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users/'
        self.auth = ('admin', 'lcfwku1220')

    def test_001_get_user(self):
        logger.info('test_001_get_user')
        r = requests.get(self.base_url + '1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'test001')
        self.assertEqual(result['email'], 'test001@admin.com')

    def test_002_add_user(self):
        logger.info('test_002_add_user')
        data = {'id': 3, 'username': 'test003', 'email': 'test003@admin.com',
                'groups': 'http://127.0.0.1:8000/groups/2/'}
        r = requests.post(self.base_url, data=data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'test003')
        self.assertEqual(result['email'], 'test003@admin.com')

    def test_003_delete_user(self):
        logger.info('test_003_delete_user')
        r = requests.delete(self.base_url + '3/', auth=self.auth)
        self.assertEqual(r.status_code, 204)

    def test_004_update_user(self):
        logger.info('test_004_updata_user')
        data = {'email': '110@admin.com'}
        r = requests.patch(self.base_url + '2/', data=data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['email'], '110@admin.com')

    def test_005_no_auth(self):
        logger.info('test_005_no_auth')
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['detail'], '身份认证信息未提供。')


class GroupTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups/'
        self.auth = ('admin', 'lcfwku1220')

    def test_001_get_group(self):
        logger.info('test_001_get_group')
        r = requests.get(self.base_url + '1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'Developer')

    def test_002_add_group(self):
        logger.info('test_002_add_group')
        data = {'name': 'Boss'}
        r = requests.post(self.base_url, data=data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'Boss')

    def test_004_update_group(self):
        logger.info('test_004_updata_group')
        data = {'name': 'Pm'}
        r = requests.patch(self.base_url + '2/', data=data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'Pm')

    def test_003_delete_group(self):
        logger.info('test_003_delete_group')
        r = requests.delete(self.base_url + '1/', auth=self.auth)
        self.assertEqual(r.status_code, 204)


if __name__ == '__main__':
    unittest.main()
    db = DB()
    db.init_data()
