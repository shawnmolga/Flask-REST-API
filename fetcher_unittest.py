# tests/test_basic.py

import unittest
from specific_ip_fetcher import fetch_binding
import random


class FlaskTestCase(unittest.TestCase):

    input_1 = [{'url': 'http://hyver-security.com'}]
    expected_output_1=[{'url': 'http://hyver-security.com', 'text': '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>Hyver Security</title>\n    <meta name="description" content="RED TEAM INTELLIGENCE">\n    <meta name="keywords" content="Cyber security ,Cyber , Information Security , Hackers , pentest , continuous pentest, pen testing">\n    <link rel="stylesheet" href="js/bootstrap.min.css"/>\n    <link rel="stylesheet" href="js/bootstrap-theme.min.css"/>\n    <link rel="stylesheet" href="css/app.css"/>\n\n    <script src="js/jquery-2.2.4.min.js"></script>\n    <script src="js/bootstrap.min.js"></script>\n    <script src="js/index.js"></script>\n    <style>\n    </style>\n</head>\n<body>\n\n</body>\n</html>'}]

    input_2 = [{"url" : "https://hyver-security.com"},
            {"url" : "https://hyver-security.com", "target_ip" : "127.0.0.1"}]
    expected_output_2 = [{'url': 'https://hyver-security.com', 'text': '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>Hyver Security</title>\n    <meta name="description" content="RED TEAM INTELLIGENCE">\n    <meta name="keywords" content="Cyber security ,Cyber , Information Security , Hackers , pentest , continuous pentest, pen testing">\n    <link rel="stylesheet" href="js/bootstrap.min.css"/>\n    <link rel="stylesheet" href="js/bootstrap-theme.min.css"/>\n    <link rel="stylesheet" href="css/app.css"/>\n\n    <script src="js/jquery-2.2.4.min.js"></script>\n    <script src="js/bootstrap.min.js"></script>\n    <script src="js/index.js"></script>\n    <style>\n    </style>\n</head>\n<body>\n\n</body>\n</html>'},
                         {'url': 'https://hyver-security.com', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'}]


    input_3 = [{"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                {"url" : "https://hyver-security.com?r={}".format(random.randint(1, 100)), "target_ip" : "127.0.0.1"},
                ]
    expected_output_3 = [{'url': 'https://hyver-security.com?r=79', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=10', 'target_ip': '127.0.0.1', 'text':'<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=62', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=86', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><imgsrc="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=42', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=50', 'target_ip': '127.0.0.1', 'text':'<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=40', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=3', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=86', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'},
                       {'url': 'https://hyver-security.com?r=70', 'target_ip': '127.0.0.1', 'text': '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'}]

    def test_input_empty_list(self):
        res = fetch_binding.fetch_binding([])
        self.assertEqual(res, [])

    def test_input_wrong_input(self):
        res = fetch_binding.fetch_binding("")
        self.assertEqual(res, [{'error':'wrong format'}])

    def test_input_empty_dictionary(self):
        res=fetch_binding.fetch_binding([{}])
        self.assertEqual(res,[{'error' : 'wrong format'}])

    def test_input_bad_url(self):
        res=fetch_binding.fetch_binding([{'url':'http://'}])
        self.assertEqual(res,[{'url':'http://', 'error':'bad url'}])

    def test_input_bad_ip(self):
        res=fetch_binding.fetch_binding([{'url':'http://hyver-security.com', 'target_ip':'0'}])
        self.assertEqual(res,[{'url':'http://hyver-security.com', 'target_ip':'0', 'error':'bad ip'}])


    def test_input_good_url(self):
        res = fetch_binding.fetch_binding(self.input_1)
        self.assertEqual(res, self.expected_output_1)

    def test_input_good_url_and_ip(self):
        res = fetch_binding.fetch_binding(self.input_2)
        self.assertEqual(res, self.expected_output_2)


if __name__ == '__main__':
    unittest.main()