#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 14:23
# @Author : Administrator
# @Software: PyCharm

from zope.interface import interface
from zope.interface.declarations import implementer

#定义接口
class IHost(interface):
    def goodmorning(self,host):
        '''say good morning to host'''


@implementer(IHost)  # 继承接口
class Host:
    def goodmorning(self, guest):
        '''say good morning to guest'''
        return 'Good moning,%s!' % guest


if __name__ == '__main__':
    p = Host()
    hi = p.goodmorning('Tom')
    print(hi)