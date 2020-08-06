#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 17:13
# @Author : Administrator
# @Software: PyCharm

import unittest
import requests, json


class GetEventListTest(unittest.TestCase):
    '''查询发布会信息（带用户认证）'''

    # def setUp(self):
    #     self.base_url = 'http://127.0.0.1:8000/api/sec_get_event_list/'
    #     self.auth_user = ('admin', '123456')
    #
    # def test_get_event_list_auth_null(self):
    #     ''' auth为空 '''
    #     r = requests.get(self.base_url, params={'eid': ''})
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['status'], 10011)
    #     self.assertEqual(result['message'], 'user auth null')
    #
    # def test_get_event_list_eid_null(self):
    #     ''' eid 参数为空 '''
    #     r = requests.get(self.base_url, auth=self.auth_user, params={'eid':''})
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['status'], 10021)
    #     self.assertEqual(result['message'], 'parameter error')


    # def test_get_event_list_eid_success(self):
    #     '''根据eid查询成功'''
    #     r = requests.get(self.base_url, auth=self.auth_user, params={'eid': 1})
    #     result = r.json()
    #     # print(result)
    #     self.assertEqual(result['status'], 200)



if __name__ == '__main__':
    unittest.main()
