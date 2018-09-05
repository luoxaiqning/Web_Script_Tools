import Web_Logic
import Initialize_logic
import time
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *

def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Open_Login_Page(self):
	self.open_url = 'https://en.ogame.gameforge.com//main/loginError'
	self.load(QUrl(self.open_url))

def Login(self):
	self.open_url= 'https://'+self.ser_id+'-en.ogame.gameforge.com/game/index.php?page=overview&relogin=1&loginType=email'
	document 	 = self.page().mainFrame().documentElement()
	ser_id 		 = document.findFirst('option[value="'+self.ser_id+'-en.ogame.gameforge.com"]')
	username 	 = document.findFirst('input[id="usernameLogin"]')
	password 	 = document.findFirst('input[id="passwordLogin"]')
	login_button = document.findFirst('input[id="loginSubmit"]')
	ser_id.setAttribute('selected', 'selected')
	username.setAttribute('value', self.username)
	password.setAttribute('value', self.password)
	login_button.evaluateJavaScript("this.click()")


