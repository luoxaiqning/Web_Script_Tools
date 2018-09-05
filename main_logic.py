import time
import random
import traceback
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Action_List():
	action_type		=''
	url				=''
	element_path 	=''
	elements_path 	=''
	element_path_type  =''
	elements_path_type =''
	element_input_text =''
	elements_input_text=''
		

class Main():
	def __init__(self):
		firefoxProfile=FirefoxProfile() 								# 	
		#firefoxProfile.set_preference('permissions.default.image',2)	# 
		self.driver=webdriver.Firefox(firefoxProfile)
		self.driver.set_page_load_timeout(20)
		self.driver.set_window_size(500,500)

		self.element=''
		self.elements=''
		self.action_list={}

		self.Get_Action_List()
		self.Process_Action()

	def Get_Action_List(self):
		file = open('Action_List.txt','r')
		content = file.readlines()
		file.close()
		
		index=''
		for count in range(0,len(content)):
			action=content[count].split(',')[1].replace('\n','')
			detail=content[count].split(',')[2].replace('\n','')

			if index!=int(content[count].split(',')[0].replace('\n','')):
				index=int(content[count].split(',')[0].replace('\n',''))
				self.action_list[index]=Action_List()
			if   action=='action_type':
				self.action_list[index].action_type=detail
			elif action=='url':
				self.action_list[index].url=detail
			elif action=='element_path':
				self.action_list[index].element_path=detail
			elif action=='elements_path':
				self.action_list[index].elements_path=detail
			elif action=='element_path_type':
				self.action_list[index].element_path_type=detail
			elif action=='elements_path_type':
				self.action_list[index].elements_path_type=detail
			elif action=='element_input_text':
				self.action_list[index].element_input_text=detail
			elif action=='elements_input_text':
				self.action_list[index].elements_input_text=detail


		
	def Process_Action(self):
		for count in range(0,len(self.action_list)):
			action=self.action_list[count]
			if   action.action_type=='open_page':
				self.open_url(action)
			elif action.action_type=='get_element':
				self.get_element(action)
			elif action.action_type=='element_input_text':
				self.element_input_text(action)
			elif action.action_type=='click_button':
				self.click_button()
			#time.sleep(2)

	def click_button(self):
		self.element.send_keys(Keys.ENTER)

	def element_input_text(self,action):
		self.element.send_keys(action.element_input_text)

	def get_element(self,action):
		if   action.element_path_type=='by_id':
			self.element=self.driver.find_element_by_id(action.element_path)
		elif action.element_path_type=='class_name':
			self.element=self.driver.find_element_by_class_name(action.element_path)
		elif action.element_path_type=='xpath':
			self.element=self.driver.find_element_by_xpath(action.element_path)

	def open_url(self,action):
		try:
			self.driver.get(action.url)
		except TimeoutException:
			print 'page stop'

if __name__ == "__main__":
	main=Main()
