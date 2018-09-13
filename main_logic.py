import time
import random
import traceback
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)  
sys.setdefaultencoding('utf8')   

class Action_List():
	action_type		=''
	element_path_type 	=''
	element_path 	=''
	contents  		=''
	sleep_time 		=''
	goto_step 		=''
		

class Main():
	def __init__(self):
		firefoxProfile=FirefoxProfile() 								# 	
		#firefoxProfile.set_preference('permissions.default.image',2)	# 
		#self.driver=webdriver.Firefox(firefoxProfile)
		self.driver=webdriver.Chrome()
		self.driver.set_page_load_timeout(20)
		self.driver.set_window_size(500,500)
		self.element=''
		self.elements=''

		self.Get_Action_List()
		self.Process_Action()

	def Get_Action_List(self):
		file = open('Action_List1.csv','r')
		text = file.readlines()
		file.close()
		self.action_list={}

		for action_step in text[1:]:
			step_index  =int(action_step.split(',')[0].replace('\n',''))
			action_type =action_step.split(',')[1].replace('\n','')
			element_path_type=action_step.split(',')[2].replace('\n','')
			element_path=action_step.split(',')[3].replace('\n','')
			contents 	=action_step.split(',')[4].replace('\n','')[1:]
			sleep_time 	=action_step.split(',')[5].replace('\n','')
			if sleep_time=='':sleep_time=int(1)
			else:sleep_time=int(sleep_time)
			goto_step 	=action_step.split(',')[6].replace('\n','')

			self.action_list[step_index]=Action_List()
			self.action_list[step_index].action_type =action_type
			self.action_list[step_index].element_path_type=element_path_type
			self.action_list[step_index].element_path=element_path
			self.action_list[step_index].contents 	 =contents
			self.action_list[step_index].sleep_time  =sleep_time
			self.action_list[step_index].goto_step 	 =goto_step

	def Process_Action(self):
		step_index = 0
		while step_index < len(self.action_list):
			action=self.action_list[step_index]
			print 'action_type:',action.action_type
			step_index+=1
			
			if   action.action_type=='open_page':
				self.open_url(action)
			elif action.action_type=='input_text':
				self.get_element(action)
				self.element_input_text(action)
			elif action.action_type=='click_button':
				self.get_element(action)
				self.click_button()
			elif action.action_type=='download_img':
				self.get_elements(action)
				self.download_img()
			elif action.action_type=='get_html':
				self.get_html()

			if action.goto_step!='':
				step_index = int(action.goto_step)
			
			time.sleep(action.sleep_time)

		print 'end'

	def download_img(self):
		import urllib
		for element in self.elements:
			img_url=element.get_attribute('src')
			img_url=img_url.replace('thumb180','large')
			print img_url
			
			name='img/'+img_url.split('.')[-2].split('/')[-1]+'.'+img_url.split('.')[-1]
			urllib.urlretrieve(img_url,name)

	def get_html(self):
		html=self.driver.execute_script("return document.documentElement.outerHTML")
		file=open('test.html','w')
		file.write(html)
		file.close()

	def click_button(self):
		self.element.send_keys(Keys.ENTER)
		#self.element.click()

	def element_input_text(self,action):
		self.element.send_keys(action.contents)

	def get_element(self,action):
		if   action.element_path_type=='by_id':
			self.element=self.driver.find_element_by_id(action.element_path)
		elif action.element_path_type=='class_name':
			self.element=self.driver.find_element_by_class_name(action.element_path)
		elif action.element_path_type=='xpath':
			self.element=self.driver.find_element_by_xpath(action.element_path)
		elif action.element_path_type=='tag_name':
			self.element=self.driver.find_element_by_tag_name(action.element_path)

	def get_elements(self,action):
		if   action.element_path_type=='by_id':
			self.elements=self.driver.find_elements_by_id(action.element_path)
		elif action.element_path_type=='class_name':
			self.elements=self.driver.find_elements_by_class_name(action.element_path)
		elif action.element_path_type=='xpath':
			self.elements=self.driver.find_elements_by_xpath(action.element_path)
		elif action.element_path_type=='tag_name':
			self.elements=self.driver.find_elements_by_tag_name(action.element_path)

	def open_url(self,action):
		try:
			self.driver.get(action.contents)
		except TimeoutException:
			print 'page stop'

if __name__ == "__main__":
	main=Main()
