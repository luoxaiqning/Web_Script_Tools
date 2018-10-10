import sys
sys.path.append('E:\\Web_Script_Tools')
import main_logic
class account():
	city_id=''
	city_name=''
class town():
	town_name=''
	town_id=''
	class main():
		population=''
		citizens=''
		action_points=''
	class building():
		name=''
		level=''
		location=''
	class resource():
		wood=''
		wine=''
		marble=''
		glass=''
		sulfur=''
	class island_resource():
		test=''

class Main():
	def __init__(self):
		self.main=main_logic.Main()
		#login
		city_list=self.action('login')
		'''
		for index in test:
			print index,test[index]
		'''
		self.main.driver.quit()


	def action(self,action):
		action=action+'.txt'
		self.main.Get_Action_List(action)
		self.main.Process_Action()
		return self.main.return_contents

if __name__ == "__main__":
	main=Main()
