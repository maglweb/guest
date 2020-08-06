#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 18:35
# @Author : Administrator
# @Software: PyCharm

import hashlib

md5 = hashlib.md5()
sign_str = '@admin123'
sign_byte_utf8 = sign_str.encode(encoding='utf-8')
md5.update(sign_byte_utf8)
print(md5.hexdigest())