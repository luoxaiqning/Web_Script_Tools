import Login_logic
import Building_Mode_Logic
import OverView_Mode_logic
import time
import traceback

def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Login():
	print Get_time(),'Start Login'
	html = Login_logic.Login()
	return html

def Main():
	#Run('123')
	while True:
		#try:
			html = Login()
			Run(html)
		#except:
		#	traceback.print_exc()
		#	print Get_time(),'Error, Retry'

def Run(html):
	print Get_time(),'Get planet list'
	OverView_Mode_logic.Get_Planet_List(html)
	'''
	print Get_time(),'Get planet resources building level'
	OverView_Mode_logic.Get_Planet_Building_Level()
	print Get_time(),'Get planet facilities building level'
	OverView_Mode_logic.Get_Planet_Facilities_Level()
	print Get_time(),'Get planet fleet'
	OverView_Mode_logic.Get_Planet_Fleet()
	print Get_time(),'Get planet defense'
	OverView_Mode_logic.Get_Planet_Defense()
	print Get_time(),'Run Builing Mode'
	Building_Mode_Logic.Point_To_Construction()
	Building_Mode_Logic.Point_To_Production()
	'''
	print Get_time(),'Run Loot Mode'
	Building_Mode_Logic.Loot_Mode()
	print Get_time(),'Sleep 600s'
	time.sleep(600)
	
Main()