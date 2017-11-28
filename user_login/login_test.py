# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
class Login_Demo(unittest.TestCase):
	def setUp(self):
		#打开浏览器和网页
		baseurl = "http://www.1kkk.com/"
		self.driver =  webdriver.Chrome()
		self.driver.get(baseurl)
		sleep(1)

	def user_info(self):
		#读取用户信息表读取用户名和密码
		with open("information.txt") as information:
			lines = information.readlines()
			line = lines[0]
			message = line.split()
			self.username = message[0]
			self.password = message[1]

	def judge_success(self):
		#释放iframe，重新回到主页
		# self.driver.switch_to.default_content()
		flag = True
		try:
			self.driver.find_element_by_link_text("jingel")
			print 'login successful....'
			return True
		except:
			error_message = self.driver.find_element_by_id("ErrorDivShow").text
			print error_message
			flag = False
			print "login failed...."
			return flag

	def login(self,username,password):
		#用户登录
			login_btn = self.driver.find_element_by_link_text(u"登录")
			login_btn.click()
			sleep(3)
			#切换到iframe
			# self.driver.switch_to_frame("x-URS-iframe")
			# sleep(1)
			#输入用户名
			uname = self.driver.find_element_by_name("txt_name")
			uname.clear()
			uname.send_keys(username)
			sleep(1)

			#输入密码
			pwd = self.driver.find_element_by_name("txt_password")
			pwd.clear()
			pwd.send_keys(password)
			sleep(1)

			#点击登录按钮
			login_in = self.driver.find_element_by_name("loginbt")
			login_in.click()
			sleep(5)

	def test_login_success(self):
		self.login("jingel","123456")
		self.judge_success()
	
	def test_login_error(self):
		self.login("qwer","qwer")
		self.judge_success()

	def test_login_null(self):
		self.login("","")
		self.judge_success()

	def test_login_uname_null(self):
		self.login("","123456")
		self.judge_success()

	def test_login_pwd_null(self):
		self.login("jingel","")
		self.judge_success()

	def tearDown(self):
		#关闭浏览器退出测试
		self.driver.quit()
		


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(Login_Demo("test_login_success"))
	suite.addTest(Login_Demo("test_login_error"))
	suite.addTest(Login_Demo("test_login_null"))
	suite.addTest(Login_Demo("test_login_uname_null"))
	suite.addTest(Login_Demo("test_login_pwd_null"))
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = now + "_result.html"
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream = fp, title = "Test Report" ,description = u'用户登录测试')
	runner.run(suite)
	fp.close()
