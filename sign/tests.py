# -*- coding:UTF-8 -*-
from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User

# Create your tests here.
# class ModelTest(TestCase):
#     def setUp(self):
#         Event.objects.create(id=1,name='oneplus 3 event',status = True,limit=2000,address='beijing',start_time = '2020-08-03 02:18:22')
#         Guest.objects.create(id=1,event_id=1,realname='alen',phone='13256322145',email='adde@44.com',sign=False)
#
#     def test_event_models(self):
#         result = Event.objects.get(name='oneplus 3 event')
#         self.assertEqual(result.address,'beijing')
#         self.assertTrue(result.status)
#
#     def test_guest_models(self):
#         result = Guest.objects.get(phone='13256322145')
#         self.assertEqual(result.realname,'alen')
#         self.assertFalse(result.sign)


# class LoginActionTest(TestCase):
#     '''测试登录操作'''
#     def setUp(self):
#         User.objects.create_user('admin','admin@test.com','123456')
#
#     def test_add_admin(self):
#         '''添加用户'''
#         user = User.objects.get(username = 'admin')
#         self.assertEqual(user.username,'admin')
#         self.assertEqual(user.email,'admin@test.com')
#
#     def test_login_action_username_password_null(self):
#         '''用户名密码为空'''
#         test_data = {'username':'','password':''}
#         response = self.client.post('/login_action/',data = test_data)
#         self.assertEqual(response.status_code,200)
#         self.assertIn('username or password error!',response.content)

class EventManageTest(TestCase):
    '''发布会管理'''
    def setUp(self):
        User.objects.create_user('admin','admin@tt.com','123456')
        Event.objects.create(name='xiaomi',limit='2000',adress='beijing',status=1,start_time='2020-08-03 12:30:00')
        self.login_user = {'username':'admin','password':'123456'}

    def test_event_manage_success(self):
        '''测试发布会:xiaomi5'''

    def test_event_manage_search_success(self):
        '''测试发布会搜索'''