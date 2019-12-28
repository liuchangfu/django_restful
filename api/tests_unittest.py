# _*_ coding:utf-8 _*_
import requests
import unittest


class UserTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users/'
        self.auth = ('admin', 'lcfwku1220')

    def test_get_user(self):
        r = requests.get(self.base_url + '2', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'test1')
        self.assertEqual(result['email'], 'test1@admin.comm')

    def test_add_user(self):
        data = {'username': 'test6', 'email': 'test6@admin.com', 'groups': 'http://127.0.0.1:8000/groups/4/'}
        r = requests.post(self.base_url, data=data, auth=self.auth)
        result = r.json()
        print(result)
        self.assertEqual(result['username'], 'test6')

    def test_update_user(self):
        data = {'email': 'test3@admin.com'}
        r = requests.patch(self.base_url + '3', data=data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['email'], 'test2@admin.com')

    def test_auth(self):
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['detail'], '身份认证信息未提供。')


class GroupTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups/'
        self.auth = ('admin', 'lcfwku1220')

    def test_group_deve(self):
        r = requests.get(self.base_url + '2', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], '管理员组')

    def test_add_group(self):
        data = {'name': '产品组'}
        r = requests.post(self.base_url, auth=self.auth, data=data)
        result = r.json()
        self.assertEqual(result['name'], '产品组')

    def test_update_group(self):
        data = {'name': 'Boss'}
        r = requests.patch(self.base_url + '2', auth=self.auth, data=data)
        result = r.json()
        self.assertEqual(result['name'], 'Boss')

    def test_delete_group(self):
        r = requests.delete(self.base_url + '1', auth=self.auth)
        self.assertEqual(r.status_code, 204)


if __name__ == '__main__':
    unittest.main()
