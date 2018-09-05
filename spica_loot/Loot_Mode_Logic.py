from PyQt4.QtCore import *
import Web_Analyze_Tools
import time

def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Print_(text):
	print Get_time(),text

def Open_Galaxy_Page(self):
	self.open_url = 'https://'+self.ser_id+'-en.ogame.gameforge.com/game/index.php?page=galaxy&galaxy=1&system=1'#+str(self.system)
	self.load(QUrl(self.open_url))

def Get_ESP_List(self):
	self.timer.stop()
	#print '-------------------------------------------------\n\n\n\n\n'
	#print self.page().mainFrame().toHtml().toUtf8()
	#print '-------------------------------------------------\n\n\n\n\n'
	self.esp_list = self.page().mainFrame().documentElement().findAll('a[title="Espionage"]')
	self.Main_logic()


def Send_ESP(self):
	self.esp_index += 1
	self.timer.stop()
	self.esp_list[0].evaluateJavaScript("this.onclick()")
	self.Main_logic()
	
def Open_Message_Page(self):
	self.timer.stop()
	self.open_url = 'https://'+self.ser_id+'-en.ogame.gameforge.com/game/index.php?page=messages&tab=20&ajax=1'
	self.load(QUrl(self.open_url))

def Analyze_Message(self):
	html = self.page().mainFrame().toHtml().toUtf8()
	self.target_list = Web_Analyze_Tools.Get_Target_list(html)
	list_temp={}
	index=0
	for target in self.target_list:
		fleet     = int(self.target_list[target]['Fleets'])
		defence   = int(self.target_list[target]['Defence'])
		resources = int(self.target_list[target]['Resources'])
		koords    = self.target_list[target]['Koords']
		player    = self.target_list[target]['Player']
		status    = self.target_list[target]['Status']
		if fleet + defence <= self.loot_defence_trigeer and resources >= self.loot_resources_trigger:
			list_temp[index]=self.target_list[target]
			index+=1
	self.target_list=list_temp
	if len(self.target_list) == 0:
		Print_('no target')
		self.next_action = 'Open_Fleet_Page_ESP'
	else:
		Print_('target number: '+str(len(self.target_list)))
	self.Main_logic()


def Send_Fleets_fleet1(self):
	self.timer.stop()
	if self.target_index < len(self.target_list):
		self.loot_index+=1
		self.loot_resources += int(self.target_list[int(self.target_index)]['Resources']) / 2
		Print_('----------Loot index: '+str(self.loot_index)+' ;\tResources: '+str(self.target_list[int(self.target_index)]['Resources'])+'----------')
		#self.Refresh_Title()
		#Print_('Total loot resources: '+str(self.loot_resources))
		self.open_url = str(self.target_list[int(self.target_index)]['Url'])
		self.target_index += 1
		self.load(QUrl(self.open_url))
	else:
		self.target_index= 0
		self.next_action = 'Open_Fleet_Page_ESP'
		self.Main_logic()

def Send_Fleets_Next(self,text):
	self.timer.stop()
	self.onClick= True
	next_button = self.page().mainFrame().documentElement().findFirst('a[id="'+str(text)+'"]')
	#next_button.setAttribute('class', 'on')
	next_button.evaluateJavaScript("this.onclick()")

def Open_Fleet_Page(self):
	self.timer.stop()
	self.onClick  = True
	self.open_url = 'https://'+self.ser_id+'-en.ogame.gameforge.com/game/index.php?page=fleet2'
	self.load(QUrl(self.open_url))

def Get_Fleet_Line_ESP(self):
	status,self.lines = Web_Analyze_Tools.Get_Fleet_Line(self.page().mainFrame().toHtml().toUtf8())
	if status:
		Print_('Fleet lines: '+str(self.lines))
		self.Refresh_Title()
		self.Main_logic()
	else:
		Print_('No fleet lines')
		self.next_action = 'Open_Fleet_Page_ESP'
		self.Main_logic()

def Get_Fleet_Line_Loot(self):
	status,self.lines = Web_Analyze_Tools.Get_Fleet_Line(self.page().mainFrame().toHtml().toUtf8())
	if status:
		Print_('Fleet lines: '+str(self.lines))
		self.Refresh_Title()
		self.Main_logic()
	else:
		Print_('No fleet lines')
		self.next_action = 'Open_Fleet_Page_Loot'
		self.Main_logic()

def Get_Next_Target(self):
	file = open('Target_List.txt','r')
	target_list   = file.readlines()
	target_index  = int(target_list[0])
	target_detail = target_list[target_index].split(',')
	file.close()

	self.galaxy   = target_detail[0]
	self.system   = target_detail[1]
	self.position = target_detail[2]
	self.p_or_m   = target_detail[3]
	self.esp_list[0].setAttribute('onclick','sendShips(6,'+self.galaxy+','+self.system+','+self.position+','+self.p_or_m+',3); return false;')

	target_index = target_index + 1
	if target_index >= len(target_list):
		target_index = 1
	target_list[0]= str(target_index)+'\n'
	file = open('Target_List.txt','w+')
	file.writelines(target_list)  
	file.close()
	self.Main_logic()