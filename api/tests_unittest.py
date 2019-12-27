# _*_ coding:utf-8 _*_
import requests
import unittest


class UserTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users/'
        self.auth = ('admin', 'lcfwku1220')

    def test_get_user(self):
        r = requests.get(self.base_url + '1', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'admin')
        self.assertEqual(result['email'], 'admin@admin.com')

    def test_add_user(self):
        data = {'username': 'test5', 'email': 'test3@admin.com', 'groups': 'http://127.0.0.1:8000/groups/1/'}
        r = requests.post(self.base_url, data=data, auth=self.auth)
        result = r.json()
        print(result)
        self.assertEqual(result['username'], 'test5')

    def test_update_user(self):
        data = {'email': 'test2@admin.com'}
        r = requests.patch(self.base_url + '3', data=data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['email'], 'est2@admin.com')

    def test_auth(self):
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['detail'], '身份认证信息未提供。')


if __name__ == '__main__':
    unittest.main()
