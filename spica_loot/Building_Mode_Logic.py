import Web_Analyze_Tools
import Web_Logic
import Initialize_logic
import time
import traceback

def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Loot_Mode():
	Send_Espionage()
	'''
	text = 'abcdefg'
	Change_Notices(text)
	print Web_Analyze_Tools.Get_Notices_Text(Get_Notices())
	'''

def Send_Espionage():
	target={}
	target['Galaxy']=2
	target['System']=446
	target['Position']=8	
	fleets={}
	fleets[0]={}
	fleets[0]['Type']='am210'
	fleets[0]['Number']=1
	planet = Initialize_logic.Global_.planet_id['Homeworld']
	Web_Logic.Post_Fleet(planet,target,6,fleets)
#Send_Espionage()

def Send_Loot_Fleets():
	pass

def Get_Notices():
	post_data	= {	
					'page' 	: 'notices',  
					'id' 	: '367', 
					'show'  : 1,  
					'popup' : 0
					}
	post_url = 'https://s150-en.ogame.gameforge.com/game/index.php?page=notices'
	html = Web_Logic.Page_Openner(post_url,post_data)
	return html

def Change_Notices(text):
	token = Web_Analyze_Tools.Get_Token(Get_Notices())
	post_url = 'https://s150-en.ogame.gameforge.com/game/index.php?page=notices'
	post_data	= {	
					'id' 			: '367', 
					'save'			: 1,
					'token' 		: token,  
					'randomId' 		: '367',
					'noticeSubject' : 'test',
					'noticePrio' 	: 2,
					'noticeText'	: text
					}
	Web_Logic.Page_Openner(post_url,post_data)
	return True

def Point_To_Construction():
	point_to_construction_list = Initialize_logic.Get_Piont_To_Construction_List()
	for list_ in range(0,100):
		try:
			planet   = point_to_construction_list[list_]['Planet']
			building = point_to_construction_list[list_]['Building']
			level	 = point_to_construction_list[list_]['Level']
			type_	 = Initialize_logic.Global_.subject_type[building]
			current_level = Initialize_logic.Global_.planet_building_level[planet][building]
			print Get_time(),'Try to construction',building,'in',planet
			if int(level) > int(current_level):
				if Building_Upgrade(planet,building,type_):
					return True
			else:
				print Get_time(),planet,building,'level match'
		except:
			pass
	return True

def Building_Upgrade(planet,building,type_):
	post_url = 'https://s150-en.ogame.gameforge.com/game/index.php?page='+type_+'&cp='+Initialize_logic.Global_.planet_id[planet]
	try:
		html 	 = Web_Logic.Page_Openner(post_url,None)
		post_url = Web_Analyze_Tools.Get_Building_Upgrade_Url(html,building)
		if post_url:
			Web_Logic.Page_Openner(post_url,None)
			print Get_time(),'Start to construction',building,'in planet',planet
			return True
		else:
			print Get_time(),'There is building in construction or not enough resources'
			return False
	except:
		print Get_time(),'There is building in construction or not enough resources'
		traceback.print_exc()
		return True

def Point_To_Production():
	point_to_production_list = Initialize_logic.Get_Piont_To_Production_List()
	for list_ in range(0,100):
		try:
			planet  = point_to_production_list[list_]['Planet']
			subject = point_to_production_list[list_]['Subject']
			number	= point_to_production_list[list_]['Number']
			type_	= Initialize_logic.Global_.subject_type[subject]
			if type_== 'shipyard':
				current_number = Initialize_logic.Global_.planet_fleet[planet][subject]
			elif type_ == 'defense':
				current_number = Initialize_logic.Global_.planet_defense[planet][subject]
			production_number = int(number) - int(current_number)
			if production_number > 0:
				Subject_Production(planet,subject,production_number,type_)
		except:
			pass
	return True

def Subject_Production(planet,subject,production_number,type_):
	post_url = 'https://s150-en.ogame.gameforge.com/game/index.php?page='+type_+'&cp='+Initialize_logic.Global_.planet_id[planet]
	try:
		html  = Web_Logic.Page_Openner(post_url,None)
		token = Web_Analyze_Tools.Get_Token(html)
		post_data = {
						'token' : token,
						'modus'	: 1,
						'type'	: Initialize_logic.Global_.subject_ref[subject],
						'menge'	: production_number
		            }
		Web_Logic.Page_Openner(post_url,post_data)
		print Get_time(),'Try to production',production_number,subject,'in',planet
	except:
		traceback.print_exc()
		return True