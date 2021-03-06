import sys
import traceback
sys.path.append('E:\\Web_Script_Tools')
import main_logic
import class_pool
import re

class Main():
	def __init__(self):
		self.main=main_logic.Main()
		self.city_list={}
		self.current_city=0
		#login
		self.login()
		self.get_overview()
		self.get_trade_overview()

	def get_trade_overview(self):
		self.current_city=0
		url=str(self.city_list[self.current_city].building['TradingPost'].href)
		print url
		self.main.driver.get(url)
		self.get_trade_list()

	def get_trade_list(self):
		return_contents=self.action('get_trade_list')
		for index in return_contents['html']:
			html=return_contents['html'][index].replace(',','').replace(' ','').replace('amp;','')
			
			print re.compile('(?<=<td>)\\d*').search(html).group()
			print re.compile('(?<=title=").*?(?=">)').search(html).group()
			print re.compile('(?<=white-space:nowrap;">).*?(?=<)').search(html).group()
			print re.compile('(?<=href="\\?).*?(?=">)').search(html).group()

	def get_overview(self):
		for index in self.city_list:
			self.current_city=index
			url='https://s1-en.ikariam.gameforge.com/index.php?cityId='+str(self.city_list[self.current_city].city_id)
			self.main.driver.get(url)
			self.get_building_level()
			self.get_resources()
		
		for index in self.city_list:
			print '-----------------------------------------------------------'
			print self.city_list[index].city_id,self.city_list[index].city_name
			print 'wood',self.city_list[index].resource.wood
			print 'wine',self.city_list[index].resource.wine
			print 'marble',self.city_list[index].resource.marble
			print 'glass',self.city_list[index].resource.glass
			print 'sulfur',self.city_list[index].resource.sulfur
			for index1 in self.city_list[index].building:
				print self.city_list[index].building[index1].name,self.city_list[index].building[index1].level,self.city_list[index].building[index1].location,self.city_list[index].building[index1].href


	def login(self):
		return_contents=self.action('login')
		for index in range(0,len(return_contents['city_name'])):
			self.city_list[index]=class_pool.city_class()

		for index in self.city_list:
			self.city_list[index].city_name=return_contents['city_name'][index]
			self.city_list[index].city_id  =return_contents['city_id'][index]
			

	def get_building_level(self):
		return_contents=self.action('get_building_level')
		self.city_list[self.current_city].building={}
		number=0
		for index in return_contents['detail']:
			try:
				building=return_contents['detail'][index].replace(' ','').replace(')','').split('(')
				self.city_list[self.current_city].building[building[0]]=class_pool.city_class.building()
				self.city_list[self.current_city].building[building[0]].name=building[0]
				self.city_list[self.current_city].building[building[0]].level=building[1]
				self.city_list[self.current_city].building[building[0]].location=return_contents['location'][number]
				self.city_list[self.current_city].building[building[0]].href=return_contents['href'][number]
			except:
				pass
			number+=1

	def get_resources(self):
		return_contents=self.action('get_resources')
		self.city_list[self.current_city].resource=class_pool.city_class.resource()
		self.city_list[self.current_city].resource.wood  =return_contents['wood'][0].replace(',','')
		self.city_list[self.current_city].resource.wine  =return_contents['wine'][0].replace(',','')
		self.city_list[self.current_city].resource.marble=return_contents['marble'][0].replace(',','')
		self.city_list[self.current_city].resource.glass =return_contents['glass'][0].replace(',','')
		self.city_list[self.current_city].resource.sulfur=return_contents['sulfur'][0].replace(',','')

	def action(self,action):
		self.main.Get_Action_List(action)
		self.main.Process_Action()
		return self.main.return_contents

	def test(self):
		return_contents=self.action('test1')

if __name__ == "__main__":
	try:
		main=Main()
	except:
		print traceback.print_exc()
	main.main.driver.quit()
