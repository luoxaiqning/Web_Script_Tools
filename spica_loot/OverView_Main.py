import time
import Login_logic
import OverView_Mode_logic
import Initialize_logic
import traceback
import sys
 
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

        
def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Print_(text):
	print Get_time(),text

class WEB_UI(QWebView):
	def __init__(self):
		QWebView.__init__(self)
		self.next_action 	= 'Open_Login_Page'
		self.planet_index 	= 0
		self.resize(200,200)
		self.page().settings().setAttribute(QWebSettings.AutoLoadImages, False)
		self.page().settings().setAttribute(QWebSettings.JavascriptEnabled, True)
		self.page().mainFrame().loadFinished.connect(self.Finish_Loading)
		self.OverView_Mode_logic()
		#self.timer = QTimer()
		#self.timer.timeout.connect(self.OverView_Mode_logic)
		#self.timer.start(1000)

	def OverView_Mode_logic(self):
		#Login
		if   self.next_action == 'Open_Login_Page':
			Print_(self.next_action)
			Login_logic.Open_Login_Page(self)
			self.next_action  =  'Login'
		elif self.next_action == 'Login':
			Print_(self.next_action)
			self.next_action  =  'Get_Planet_List'
			Login_logic.Login(self)

		#Get planet list
		elif self.next_action == 'Get_Planet_List':
			Print_(self.next_action)
			self.next_action  =  'Open_OverView_Page'
			OverView_Mode_logic.Get_Planet_List(self)
			
		#Get planet resources
		elif self.next_action == 'Open_OverView_Page':
			Print_(self.next_action)
			self.next_action  =  'Get_Planet_Resources'
			OverView_Mode_logic.Open_Every_Planets_Page(self,'overview')
		elif self.next_action == 'Get_Planet_Resources':
			Print_(self.next_action)
			self.next_action  =  'Open_OverView_Page'
			OverView_Mode_logic.Get_Planet_Resources(self)
			if  self.planet_index>= len(Initialize_logic.Global_.planet_id):
				self.planet_index=  0
				self.next_action =  'Open_Building_Page'
			self.OverView_Mode_logic()

		#Get planet resources building level
		elif self.next_action == 'Open_Building_Page':
			Print_(self.next_action)
			self.next_action  =  'Get_Planet_Building_Level'
			OverView_Mode_logic.Open_Every_Planets_Page(self,'resources')
		elif self.next_action == 'Get_Planet_Building_Level':
			Print_(self.next_action)
			self.next_action  =  'Open_Building_Page'
			OverView_Mode_logic.Get_Planet_Building_Level(self,'resources')
			if  self.planet_index>= len(Initialize_logic.Global_.planet_id):
				self.planet_index=  0
				self.next_action =  'Open_Facilities_Page'
			self.OverView_Mode_logic()

		#Get planet facilities building level
		elif self.next_action == 'Open_Facilities_Page':
			Print_(self.next_action)
			self.next_action  =  'Get_Planet_Facilities_Level'
			OverView_Mode_logic.Open_Every_Planets_Page(self,'station')
		elif self.next_action == 'Get_Planet_Facilities_Level':
			Print_(self.next_action)
			self.next_action  =  'Open_Facilities_Page'
			OverView_Mode_logic.Get_Planet_Building_Level(self,'station')
			if  self.planet_index>= len(Initialize_logic.Global_.planet_id):
				self.planet_index=  0
				self.next_action =  'Open_Shipyard_Page'
			self.OverView_Mode_logic()

		#Get planet fleets detail
		elif self.next_action == 'Open_Shipyard_Page':
			Print_(self.next_action)
			self.next_action  =  'Get_Planet_Fleet'
			OverView_Mode_logic.Open_Every_Planets_Page(self,'shipyard')
		elif self.next_action == 'Get_Planet_Fleet':
			Print_(self.next_action)
			self.next_action  =  'Open_Shipyard_Page'
			OverView_Mode_logic.Get_Planet_Fleet(self)
			if  self.planet_index>= len(Initialize_logic.Global_.planet_id):
				self.planet_index=  0
				self.next_action =  'Open_Defense_Page'
			self.OverView_Mode_logic()

		#Get planet defense detail
		elif self.next_action == 'Open_Defense_Page':
			Print_(self.next_action)
			self.next_action  =  'Get_Planet_Defense'
			OverView_Mode_logic.Open_Every_Planets_Page(self,'defense')
		elif self.next_action == 'Get_Planet_Defense':
			Print_(self.next_action)
			self.next_action  =  'Open_Defense_Page'
			OverView_Mode_logic.Get_Planet_Defense(self)
			if  self.planet_index>= len(Initialize_logic.Global_.planet_id):
				self.planet_index=  0
				self.next_action =  'Print_OverView'
			self.OverView_Mode_logic()

		#Print overview
		elif self.next_action == 'Print_OverView':
			Print_(self.next_action)
			OverView_Mode_logic.Print_OverView()

	def Finish_Loading(self):
		self.current_url = self.page().mainFrame().documentElement().evaluateJavaScript('document.location.href').toString()
		self.current_html= self.page().mainFrame().toHtml().toUtf8()
		#print 'open_url:\t\t',self.open_url
		#print 'current_url:\t',self.current_url
		if self.open_url == self.current_url:
			self.OverView_Mode_logic()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WEB_UI()
    browser.show()
    app.exec_()
