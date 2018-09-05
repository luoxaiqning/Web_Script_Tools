import time
import Login_logic
import OverView_Mode_logic
import Loot_Mode_Logic
import Initialize_logic
import traceback
import sys

from PyQt4.QtGui import *
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
		self.debug_index = 0
		self.debug_text  = ''
		self.next_action = 'Open_Login_Page'
		self.target_index= 0
		self.esp_index   = 1
		self.onClick 	 = False
		self.lines 		 = 0	
		self.loot_index  = 0
		self.esp_index2  = 0
		self.monitor_status = False
		self.loot_resources = 0
		self.galaxy      = 1
		self.system      = 1
		self.position    = 1
		self.p_or_m      = 1
		self.lines       = 10
		self.load_setup()
		self.resize(1200,200)
		self.setWindowIcon(QIcon('ogame.png'))
		self.setWindowTitle('Ogame')
		self.page().settings().setAttribute(QWebSettings.AutoLoadImages, False)
		self.page().settings().setAttribute(QWebSettings.JavascriptEnabled, True)
		self.page().mainFrame().loadFinished.connect(self.Finish_Loading)
		self.monitor_timer = QTimer()
		self.monitor_timer.timeout.connect(self.monitor)
		self.monitor_timer.start(self.time_relogin)
		self.Main_logic()

	def load_setup(self):
		file = open('Setup.txt','r')
		text = file.readlines()
		self.ser_id   				= str(text[0].split(':')[1]).replace('\n','')
		self.username 				= str(text[1].split(':')[1]).replace('\n','')
		self.password 				= str(text[2].split(':')[1]).replace('\n','')
		self.time_relogin 			= int(text[3].split(':')[1])
		self.time_get_fleet_line	= int(text[4].split(':')[1])
		self.time_esp_low 			= int(text[5].split(':')[1])
		self.time_esp_top 			= int(text[6].split(':')[1])
		self.time_analyze_message 	= int(text[7].split(':')[1])
		self.time_get_esp_target	= int(text[8].split(':')[1])
		self.loot_resources_trigger	= int(text[9].split(':')[1])
		self.loot_defence_trigeer 	= int(text[10].split(':')[1])
		self.loot_galaxy_from 		= int(text[11].split(':')[1])
		self.loot_galaxy_to 		= int(text[12].split(':')[1])
		file.close()
		
	def monitor(self):
		if self.monitor_status:
			print 'relogin'
			self.next_action = 'Open_Login_Page'
			self.target_index= 0
			self.onClick 	 = False
			self.lines 		 = 0	
			self.Main_logic()
		else:
			self.monitor_status = True

	def Main_logic(self):
		self.load_setup()
		#Print_(self.next_action)
		self.Refresh_Title()
		self.monitor_status = False
		#Login----------------------------------------------------
		if   self.next_action == 'Open_Login_Page':
			Login_logic.Open_Login_Page(self)
			self.next_action  =  'Login'
		elif self.next_action == 'Login':
			self.next_action  =  'Open_Fleet_Page_ESP'
			Login_logic.Login(self)
		#---------------------------------------------------------


		#Loot-----------------------------------------------------
		#Get fleet line
		elif self.next_action == 'Open_Fleet_Page_ESP':
			self.next_action  =  'Get_Fleet_Line_ESP'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Open_Fleet_Page)
			self.timer.start(100000/(self.lines+1))
		elif self.next_action == 'Get_Fleet_Line_ESP':
			self.next_action  =  'Open_Galaxy_Page'
			Loot_Mode_Logic.Get_Fleet_Line_ESP(self)

		#Open galaxy page
		elif self.next_action == 'Open_Galaxy_Page':
			self.next_action  =  'Get_ESP_List'
			Loot_Mode_Logic.Open_Galaxy_Page(self)
		elif self.next_action == 'Get_ESP_List':
			self.next_action  =  'Get_Next_Target'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Get_ESP_List)
			self.timer.start(3000)

		#Get next target
		elif self.next_action == 'Get_Next_Target':
			self.next_action  =  'Send_ESP'
			if self.esp_index > 10:
				self.esp_index  = 1
				self.next_action= 'Open_Message_Page'
				self.Main_logic()
			else:
				Loot_Mode_Logic.Get_Next_Target(self)

		#Send ESP
		elif self.next_action == 'Send_ESP':
			self.next_action  =  'Get_Next_Target'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Send_ESP)
			self.timer.start(110000/(self.lines+1))

		#Get and analyze message
		elif self.next_action == 'Open_Message_Page':
			self.next_action  =  'Analyze_Message'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Open_Message_Page)
			self.timer.start(self.time_analyze_message)
		elif self.next_action == 'Analyze_Message':
			self.next_action  =  'Open_Fleet_Page_Loot'
			Loot_Mode_Logic.Analyze_Message(self)

		#Get fleet line
		elif self.next_action == 'Open_Fleet_Page_Loot':
			self.next_action  =  'Get_Fleet_Line_Loot'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Open_Fleet_Page)
			self.timer.start(100000/(self.lines+1))
		elif self.next_action == 'Get_Fleet_Line_Loot':
			self.next_action  =  'Send_Fleets_fleet1'
			Loot_Mode_Logic.Get_Fleet_Line_Loot(self)

		#Send loot fleets
		elif self.next_action == 'Send_Fleets_fleet1':
			self.next_action  =  'Send_Fleets_fleet2'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Send_Fleets_fleet1)
			self.timer.start(3000)
		elif self.next_action == 'Send_Fleets_fleet2':
			self.next_action  =  'Send_Fleets_fleet3'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Send_Fleets_fleet2)
			self.timer.start(3000)
		elif self.next_action == 'Send_Fleets_fleet3':
			self.next_action  =  'Send_Fleets_movement'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Send_Fleets_fleet3)
			self.timer.start(3000)
		elif self.next_action == 'Send_Fleets_movement':
			self.next_action  =  'Get_Fleet_Line_Loot'
			self.timer = QTimer()
			self.timer.timeout.connect(self.Send_Fleets_movement)
			self.timer.start(3000)
		#---------------------------------------------------------

	def Refresh_Title(self):
		text = str(self.username)
		text = text + '---Current action: '+self.next_action
		text = text + '---Free fleet lines: '+str(self.lines)
		text = text + '---Loot index: '+str(self.loot_index)
		text = text + '---Total loot resources(estimate): '+str(self.loot_resources)
		text = text + '---ESP index: '+str(self.esp_index2)
		text = text + '---ESP koords: ['+str(self.galaxy)+':'+str(self.system)+':'+str(self.position)+']'
		self.setWindowTitle(text)

	def Send_Fleets_fleet1(self):
		self.monitor_status = False
		Loot_Mode_Logic.Send_Fleets_fleet1(self)

	def Send_Fleets_fleet2(self):
		self.monitor_status = False
		Loot_Mode_Logic.Send_Fleets_Next(self,'continue')

	def Send_Fleets_fleet3(self):
		self.monitor_status = False
		Loot_Mode_Logic.Send_Fleets_Next(self,'continue')

	def Send_Fleets_movement(self):
		self.monitor_status = False
		Loot_Mode_Logic.Send_Fleets_Next(self,'start')

	def Send_ESP(self):
		self.esp_index2 += 1
		self.Refresh_Title()
		self.monitor_status = False
		#Print_('ESP: '+str(self.esp_index)+' galaxy: '+self.galaxy+' system: '+self.system+' position:'+self.position)
		Loot_Mode_Logic.Send_ESP(self)

	def Open_Message_Page(self):
		self.monitor_status = False
		Loot_Mode_Logic.Open_Message_Page(self)

	def Open_Fleet_Page(self):
		self.monitor_status = False
		Loot_Mode_Logic.Open_Fleet_Page(self)

	def Get_ESP_List(self):
		self.monitor_status = False
		Loot_Mode_Logic.Get_ESP_List(self)

	def Print_Html(self):
		print self.page().mainFrame().documentElement().evaluateJavaScript('document.location.href').toString()
		print self.page().mainFrame().toHtml().toUtf8()
		self.timer.stop()

	def Finish_Loading(self):
		self.current_url = self.page().mainFrame().documentElement().evaluateJavaScript('document.location.href').toString()
		#self.current_html= self.page().mainFrame().toHtml().toUtf8()
		#print 'open_url:\t\t',self.open_url
		#print 'current_url:\t',self.current_url
		if self.open_url == self.current_url or self.onClick:
			#print 'self.onClick',self.onClick
			self.monitor_status = False
			self.onClick = False
			self.Main_logic()




if __name__ == "__main__":
	app = QApplication(sys.argv)
	browser = WEB_UI()
	browser.show()
	app.exec_()
