#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 14:18
# @Author : Administrator
# @Software: PyCharm

class Host(object):
    def goodmorning(self,name):
        return 'Good morning,%s!'%name

if __name__ == '__main__':
    h = Host()
    hi = h.goodmorning('ma')
    print(hi)
