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
		
		self.test()

	def test(self):
		return_contents=self.action('test1')
		for index in return_contents['html']:
			print '-----------------------------------------'
			print index
			print return_contents['html'][index]

		

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
'''
if __name__ == "__main__":
	try:
		main=Main()
	except:
		print traceback.print_exc()
	main.main.driver.quit()
'''
html='\
                                    <td class="short_text80">G Troop 11 MM                                        <br>(M Sqdn)\
                                    </td>\
                                                                        <td>242,500</td>\
                                    <td><img src="skin/resources/icon_wine.png" alt="Wine" title="Wine"></td>\
                                    <td style="white-space:nowrap;">6                                        <img src="skin/resources/icon_gold.png" class="icon_gold"> Per Piece</td>\
                                    <td>8</td>\
                                    <td><a onclick="ajaxHandlerCall(this.href);return false;" href="?view=takeOffer&amp;destinationCityId=448470&amp;oldView=branchOffice&amp;activeTab=bargain&amp;cityId=769529&amp;position=9&amp;type=333&amp;resource=1"><img src="skin/layout/icon-kiste.png" alt="" title=""></a></td>\
                                '
html=html.replace(',','').replace(' ','').replace('amp;','')
print html
print re.compile('(?<=<td>)\\d*').search(html).group()
print re.compile('(?<=title=").*?(?=">)').search(html).group()
print re.compile('(?<=white-space:nowrap;">).*?(?=<)').search(html).group()
print re.compile('(?<=href="\\?).*?(?=">)').search(html).group()