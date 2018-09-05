import Web_Analyze_Tools
import Web_Logic
import time
import Initialize_logic
from PyQt4.QtCore import *

def Get_Planet_List(self):
	Web_Analyze_Tools.Get_Planet_List(self.page().mainFrame().toHtml().toUtf8())
	print Initialize_logic.Global_.planet_id
	for planet in Initialize_logic.Global_.planet_id:
		Initialize_logic.Global_.planet_resources[planet] = {'':''}
		Initialize_logic.Global_.planet_building_level[planet] = {'':''}
		Initialize_logic.Global_.planet_fleet[planet] = {'':''}
		Initialize_logic.Global_.planet_defense[planet] = {'':''}

def Open_Every_Planets_Page(self,text):
	self.planet_index += 1
	local_index = 0
	for planet in Initialize_logic.Global_.planet_id:
		local_index += 1
		if local_index <= self.planet_index:
			self.current_planet_name= planet
			self.current_planet_id  = Initialize_logic.Global_.planet_id[planet]
	self.open_url = 'https://s150-en.ogame.gameforge.com/game/index.php?page='+text+'&cp='+str(self.current_planet_id)
	self.load(QUrl(self.open_url))

def Get_Planet_Resources(self):
	Initialize_logic.Global_.planet_resources[self.current_planet_name]['Metal'] 	 = Web_Analyze_Tools.Get_Planet_Resources(self.current_html,'resources_metal')
	Initialize_logic.Global_.planet_resources[self.current_planet_name]['Crystal'] 	 = Web_Analyze_Tools.Get_Planet_Resources(self.current_html,'resources_crystal')
	Initialize_logic.Global_.planet_resources[self.current_planet_name]['Deuterium'] = Web_Analyze_Tools.Get_Planet_Resources(self.current_html,'resources_deuterium')
	Initialize_logic.Global_.planet_resources[self.current_planet_name]['Energy'] 	 = Web_Analyze_Tools.Get_Planet_Resources(self.current_html,'resources_energy')
	Initialize_logic.Global_.planet_resources[self.current_planet_name]['Darkmatter']= Web_Analyze_Tools.Get_Planet_Resources(self.current_html,'resources_darkmatter')


def Get_Planet_Building_Level(self,text):
	for subject in Initialize_logic.Global_.subject_type:
		if Initialize_logic.Global_.subject_type[subject] == text:
			level = Web_Analyze_Tools.Get_Planet_Building_Level(self.current_html,subject)
			Initialize_logic.Global_.planet_building_level[self.current_planet_name][subject] = level
	Initialize_logic.Global_.planet_building_level[self.current_planet_name]['In Construction'] = Web_Analyze_Tools.Get_Planet_In_Construction(self.current_html)


def Get_Planet_Fleet(self):
	for subject in Initialize_logic.Global_.subject_type:
		if Initialize_logic.Global_.subject_type[subject] == 'shipyard':
			current_number = Web_Analyze_Tools.Get_Planet_Fleet(self.current_html,subject)
			production_number = Web_Analyze_Tools.Get_Planet_In_Production(self.current_html,subject)
			Initialize_logic.Global_.planet_fleet[self.current_planet_name][subject] = int(current_number) + int(production_number)

def Get_Planet_Defense(self):
	for subject in Initialize_logic.Global_.subject_type:
		if Initialize_logic.Global_.subject_type[subject] == 'defense':
			current_number = Web_Analyze_Tools.Get_Planet_Defense(self.current_html,subject)
			production_number = Web_Analyze_Tools.Get_Planet_In_Production(self.current_html,subject)
			Initialize_logic.Global_.planet_defense[self.current_planet_name][subject] = int(current_number) + int(production_number)

def Print_OverView():
	print '\n------------------------------------OVERVIEW------------------------------------\n'
	for planet in Initialize_logic.Global_.planet_id:
		print '------------------',planet,Initialize_logic.Global_.planet_id[planet],Initialize_logic.Global_.planet_koords[planet],'------------------'
		for int_ in range(0,1000):
			try:
				subject_name = Initialize_logic.Global_.subject_order[int_]
				if int_ < 100:
					print 'Resources',subject_name,':',Initialize_logic.Global_.planet_resources[planet][subject_name]
				elif int_ >= 100 and int_ < 300:
					print 'Building',subject_name,':',Initialize_logic.Global_.planet_building_level[planet][subject_name]
				elif int_ >= 300 and int_ < 400:
					print 'Fleets',subject_name,':',Initialize_logic.Global_.planet_fleet[planet][subject_name]
				elif int_ >= 400 and int_ < 500:
					print 'Defense',subject_name,':',Initialize_logic.Global_.planet_defense[planet][subject_name]
			except:
				pass
	print '\n------------------------------------OVERVIEW------------------------------------\n'
	return True