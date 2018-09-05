import time
import Login_logic
import OverView_Mode_logic
import traceback

def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Login():
	print Get_time(),'Start Login'
	html = Login_logic.Login()
	return html

def Main():
	status = 0
	while status < 5:
		try:
			html = Login()
			Run(html)
			status = 99
		except:
			status += 1
			traceback.print_exc()
			print Get_time(),'Error, Retry'

def Run(html):
	print Get_time(),'Get planet list'
	OverView_Mode_logic.Get_Planet_List(html)
	print Get_time(),'Get planet resources'
	OverView_Mode_logic.Get_Planet_Resources()
	print Get_time(),'Get planet resources building level'
	OverView_Mode_logic.Get_Planet_Building_Level()
	print Get_time(),'Get planet facilities building level'
	OverView_Mode_logic.Get_Planet_Facilities_Level()
	print Get_time(),'Get planet fleet'
	OverView_Mode_logic.Get_Planet_Fleet()
	print Get_time(),'Get planet defense'
	OverView_Mode_logic.Get_Planet_Defense()
	print Get_time(),'Print OverView'
	OverView_Mode_logic.Print_OverView()

			

Main()