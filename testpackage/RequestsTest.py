#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 17:38
# @Author : Administrator
# @Software: PyCharm

import requests

r = requests.get('https://api.github.com/user',auth=('823358533@qq.com','.'))

print(r.status_code,r.headers,r.text,r.json())