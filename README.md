# Python-Selenium实战
基于python语言采用selenium+webdriver相关的知识对web执行的自动化操作实战

**更多selenium基础知识请点击此处：**[selenium基础知识](http://www.jianshu.com/nb/10193521)

- 126邮箱登录界面
	- 贴出部分代码如下：[完整代码请点击查看~](12306_web\mailloginpage.py)
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