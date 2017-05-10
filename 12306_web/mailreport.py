# -*- coding:utf-8 -*-
#导入需要的模块
from selenium import webdriver
from time import sleep
import unittest
import time #导入time模块为了之后生成的测试模板是按照时间来命名，避免直接覆盖的问题
import HTMLTestRunner  #导入生成的HTML报告模板
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
		uname = "xxxxxxxxxxxxx"#输入你的邮箱账号
		account = self.driver.find_element_by_name("email")
		account.send_keys(uname)
		sleep(2)
		pwd = "xxxxxxxx"#输入你的邮箱密码
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
 	testunit = unittest.TestSuite()
 	testunit.addTest(MailLogin("test_login"))
 	now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time())) 
 	report_path = "report"+now+".html"
 	fp = open(report_path,"wb")
 	runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u"163邮箱登录页面测试",description = u"执行结果如下显示")
 	runner.run(testunit)
 	fp.close()