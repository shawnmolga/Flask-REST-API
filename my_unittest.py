# tests/test_basic.py

import unittest
import my_api
import urllib3
import json


class FlaskTestCase(unittest.TestCase):
    username = 'admin'
    password = 'password'

    def setUp(self):
        my_api.app.config['TESTING']=True
        self.app = my_api.app.test_client()

    def test_login_no_creds(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 401)

    def test_login_wrong_creds(self):
        head = urllib3.util.make_headers(basic_auth=self.username + ":" + self.password + 'x')
        response = self.app.open('login', method='GET', headers=head)
        self.assertEqual(response.status_code, 401)


    def open_with_auth(self, url, method):
        head = urllib3.util.make_headers(basic_auth=self.username + ":" + self.password)
        return self.app.open(url,
                             method=method,
                             headers=head
                             )

    def test_login_with_creds(self):
        response = self.open_with_auth('/login', 'GET')
        self.assertEqual(response.status_code, 200)

    def test_return_val_login_with_creds(self):
        response = self.open_with_auth('/login', 'GET')
        self.assertNotEquals(response.get_json(), None)

    def test_api_no_token(self):
        response = self.app.get('/api/bindings', follow_redirects=True)
        self.assertEqual(response.status_code, 401)

    def test_api_wrong_token(self):
        head = {'x-access-token': 'wrong-token', 'content-type': 'application/json'}
        response = self.app.post('/api/bindings', data=json.dumps({}), headers=head)
        self.assertEqual(response.status_code, 401)

    def test_api_token(self):
        #TODO
        return True


if __name__ == '__main__':
    unittest.main()