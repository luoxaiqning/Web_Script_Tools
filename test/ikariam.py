import sys
import traceback
sys.path.append('E:\\Web_Script_Tools')
import main_logic
class city_class():
	city_id=''
	city_name=''
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
		self.city_list={}
		self.current_city=0
		#login
		self.login()

		for index in self.city_list:
			self.current_city=index
			url='https://s1-en.ikariam.gameforge.com/index.php?cityId='+str(self.city_list[index].city_id)
			self.mian.main.driver.get(url)
			self.get_building_level()
			self.get_resources()
		#for index in self.city_list[self.current_city].building:
		#	print self.city_list[self.current_city].building[index].name,self.city_list[self.current_city].building[index].level,self.city_list[self.current_city].building[index].location
		for index in self.city_list:
			print self.city_list[index].city_id,self.city_list[index].city_name
			print 'wood',self.city_list[index].resource.wood
			print 'wine',self.city_list[index].resource.wine
			print 'marble',self.city_list[index].resource.marble
			print 'glass',self.city_list[index].resource.glass
			print 'sulfur',self.city_list[index].resource.sulfur

	def login(self):
		return_contents=self.action('login')
		for index in range(0,len(return_contents['city_name'])):
			self.city_list[index]=city_class()

		for index in self.city_list:
			self.city_list[index].city_name=return_contents['city_name'][index]
			self.city_list[index].city_id  =return_contents['city_id'][index]
			

	def get_building_level(self):
		return_contents=self.action('get_building_level')
		self.city_list[self.current_city].building={}
		number=0
		for index in return_contents['building_detail']:
			building=return_contents['building_detail'][index].replace(' ','').replace(')','').split('(')
			self.city_list[self.current_city].building[building[0]]=city_class.building()
			self.city_list[self.current_city].building[building[0]].name=building[0]
			self.city_list[self.current_city].building[building[0]].level=building[1]
			self.city_list[self.current_city].building[building[0]].location=return_contents['building_location'][number]
			number+=1

	def get_resources(self):
		return_contents=self.action('get_resources')
		self.city_list[self.current_city].resource=city_class.resource()
		self.city_list[self.current_city].resource.wood  =return_contents['wood'][0].replace(',','')
		self.city_list[self.current_city].resource.wine  =return_contents['wine'][0].replace(',','')
		self.city_list[self.current_city].resource.marble=return_contents['marble'][0].replace(',','')
		self.city_list[self.current_city].resource.glass =return_contents['glass'][0].replace(',','')
		self.city_list[self.current_city].resource.sulfur=return_contents['sulfur'][0].replace(',','')

	def action(self,action):
		self.main.Get_Action_List(action)
		self.main.Process_Action()
		return self.main.return_contents

if __name__ == "__main__":
	try:
		main=Main()
	except:
		print traceback.print_exc()
	main.main.driver.quit()
