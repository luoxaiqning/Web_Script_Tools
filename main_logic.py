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
	element_type 	=''
	element_path 	=''
	content  		=''
		

class Main():
	def __init__(self):
		firefoxProfile=FirefoxProfile() 								# 	
		#firefoxProfile.set_preference('permissions.default.image',2)	# 
		self.driver=webdriver.Firefox(firefoxProfile)
		self.driver.set_page_load_timeout(20)
		self.driver.set_window_size(500,500)
		self.element=''
		self.elements=''

		self.Get_Action_List()
		self.Process_Action()

	def Get_Action_List(self):
		file = open('Action_List.csv','r')
		content = file.readlines()
		file.close()
		self.action_list={}

		for action_step in content[1:]:
			step_index  =int(action_step.split(',')[0].replace('\n',''))
			action_type =action_step.split(',')[1].replace('\n','')
			element_type=action_step.split(',')[2].replace('\n','')
			element_path=action_step.split(',')[3].replace('\n','')
			content 	=action_step.split(',')[4].replace('\n','')[1:]

			self.action_list[step_index]=Action_List()
			self.action_list[step_index].action_type =action_type
			self.action_list[step_index].element_type=element_type
			self.action_list[step_index].element_path=element_path
			self.action_list[step_index].content 	 =content


	def Process_Action(self):
		step_index = 0
		for step_index in range(0,len(self.action_list)):
			action=self.action_list[step_index]
			print step_index,action.element_type
			if   action.action_type=='open_page':
				self.open_url(action)
			elif action.action_type=='input_text':
				self.get_element(action)
				self.element_input_text(action)
			elif action.action_type=='click_button':
				self.get_element(action)
				self.click_button()
			elif action.action_type=='download_imgs':
				self.get_elements(action)


	def click_button(self):
		self.element.send_keys(Keys.ENTER)

	def element_input_text(self,action):
		self.element.send_keys(action.content)

	def get_element(self,action):
		if   action.element_type=='by_id':
			self.element=self.driver.find_element_by_id(action.element_path)
		elif action.element_type=='class_name':
			self.element=self.driver.find_element_by_class_name(action.element_path)
		elif action.element_type=='xpath':
			self.element=self.driver.find_element_by_xpath(action.element_path)

	def get_elements(self,action):
		if   action.element_type=='by_id':
			self.elements=self.driver.find_elements_by_id(action.element_path)
		elif action.element_type=='class_name':
			self.elements=self.driver.find_elements_by_class_name(action.element_path)
		elif action.element_type=='xpath':
			self.elements=self.driver.find_elements_by_xpath(action.element_path)

	def open_url(self,action):
		try:
			self.driver.get(action.content)
		except TimeoutException:
			print 'page stop'

if __name__ == "__main__":
	main=Main()
