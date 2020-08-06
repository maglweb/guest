#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 17:43
# @Author : Administrator
# @Software: PyCharm

import requests,unittest
#
# #查询接口地址
# url = 'http://127.0.0.1:8000/api/get_event_list/'
# r = requests.get(url,params={'eid':'1'})
# result = r.json()
#
# print(result)

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口'''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    # def test_get_event_null(self):
    #     '''发布会id为空'''
    #     r = requests.get(self.url,params={'eid':''})
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['status'],10021)

    # def test_get_event_error(self):
    #     r = requests.get(self.url,params={'eid':'sdf'})
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['status'],10022)

    def test_get_event_success(self):
        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],200)


if __name__ == '__main__':
    unittest.main()