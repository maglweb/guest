#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 11:10
# @Author : Administrator
# @Software: PyCharm


from locust import HttpLocust,TaskSet,task,HttpUser
#定义用户行为
class UserBehavior(TaskSet):
    @task(1)
    def baidu_page(self):
        self.client.get('/')


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 3000
    max_wait = 6000

#Web性能测试
# class UserBehavior(TaskSet):
#     def on_start(self):
#         '''
#         on_start is called when a Locust start before any task is scheduled
#         :return:
#         '''
#         self.Login()
#
#     def login(self):
#         self.client.post('/login_aciton',{'username':'admin','password':'123456'})
#
#     @task(1)
#     def search_phone(self):
#         self.client.get('/search_phone/',params={'phone':'13000000000'})
#
#     @task(2)
#     def guest_manage(self):
#         self.client.get('/guest_manage')
#
#     @task(2)
#     def event_manage(self):
#         self.client.get('/event_manage')
#
#
# class WebsiteUser(HttpUser):
#     task_set = UserBehavior
#     min_wait = 3000
#     max_wait = 6000

if __name__ == '__main__':
    import os
    os.system("locust -f locustfile.py --host=https://www.cnblogs.com")