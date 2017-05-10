# -*- coding:utf-8 -*-
#导入需要的模块
from selenium import webdriver
from time import sleep
import unittest
#定义函数
class MailLogin(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		base_url="http://mail.163.com/"
		self.driver.get(base_url)
		sleep(2)
	def test_login(self):
		#点击选择账号登陆
		self.driver.find_element_by_id("lbNormal").click()
		#切换到iframe上
		self.driver.switch_to_frame("x-URS-iframe")
		sleep(2)
		#切换到账号密码输入
		uname = "cheng_yuanyuan94@163.com"
		account = self.driver.find_element_by_name("email")
		account.send_keys(uname)
		sleep(2)
		pwd = "123456"
		password = self.driver.find_element_by_name("password")
		password.send_keys(pwd)
		sleep(2)
		#点击登录按钮
		lg_btn = self.driver.find_element_by_id("dologin")
		lg_btn.submit()
		sleep(2)
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
 	unittest.main()