# Python-Selenium实战
基于python语言采用selenium+webdriver相关的知识对web执行的自动化操作实战

**更多selenium基础知识请点击此处：**[selenium基础知识](http://www.jianshu.com/nb/10193521)

**[点击获得----HTMLTestRunner.py测试报告模板](http://tungwaiyip.info/software/HTMLTestRunner.html)**

------

- ###126邮箱登录界面
	- 贴出部分代码如下：详见文件夹内的py文件
<pre>
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
……
……
……
more>>>
</pre>

---
- ###126邮箱登录界面+输出测试报告
	- 贴出部分代码如下：详见文件夹内的py文件
	
<pre>
	import HTMLTestRunner  #导入生成的HTML报告模板
	testunit = unittest.TestSuite()
 	testunit.addTest(MailLogin("test_login"))
 	report_path = "report.html"
 	fp = open(report_path,"wb")
 	runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u"163邮箱登录页面测试",description = u"执行结果如下显示")
 	runner.run(testunit)
 	fp.close()
	……
	……
	……
	more>>>
</pre>
贴图如下：（可能有些人会奇怪和官网的样式不一样，不要奇怪哦，网络上有许多别人改过的哦~可以去搜索download哦）
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2539401-1a3c4f3cf5e09761.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-----
###小说登录界面（改进版）
    '''
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
    '''
贴图如下：
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2539401-321ef9c27513b8ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)