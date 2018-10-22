# coding: utf-8
import time
import random
import traceback
import Tools_Pool
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
import sys
reload(sys)  
sys.setdefaultencoding('utf8') 
class Action_List():
	action_type			=''
	element_path_type 	=''
	element_path 		=''
	contents  			=''
	sleep_time 			=''
	goto_step 			=''
	reference_flag   	=''
	url 				=''
	identify_flag 		=''
	select_type 		=''
	return_flag 		=''
	
		

class Main():
	def __init__(self):
		#firefoxProfile=FirefoxProfile() 								# 	
		#firefoxProfile.set_preference('permissions.default.image',2)	# 
		#self.driver=webdriver.Firefox(firefoxProfile)
		self.headless_flag	=True
		self.noimg_flag 	=False
		self.return_flag	=''
		chrome_options=Options()
		if self.headless_flag:chrome_options.add_argument('--headless')
		if self.noimg_flag:   chrome_options.add_experimental_option("prefs",{"profile.managed_default_content_settings.images":2})
		self.driver=webdriver.Chrome(chrome_options=chrome_options)
		#self.driver.set_page_load_timeout(120)
		#self.driver.set_window_size(500,500)

		self.element=''
		self.elements={}
		self.return_contents={}
	
	def run(self):
		try:
			self.Get_Action_List('test1')
			self.Process_Action()
			if self.headless_flag:
				self.driver.quit()
			print 'end'
		except:
			self.driver.quit()
			print 'error'
			print traceback.print_exc()
		#return self.driver

	def Get_Action_List(self,action_step):
		self.element=''
		self.elements={}
		self.return_contents={}
		print action_step
		action_step=action_step+'.txt'
		file = open(action_step,'r')
		text_list = file.readlines()
		file.close()
		text_index='0'
		step_index='0'
		self.action_list={}
		self.action_list[step_index]=Action_List()
		for text in text_list:
			text=text.replace('\n','')
			if text!='':
				text_index,text_type,text_detail=text.replace('\t','').replace(' ','').split('#')
				if int(text_index)>int(step_index):
					step_index=text_index
					self.action_list[step_index]=Action_List()
				if   text_type=='action_type'	   	:self.action_list[step_index].action_type		=str(text_detail)
				elif text_type=='url'				:self.action_list[step_index].url				=str(text_detail)
				elif text_type=='element_path_type'	:self.action_list[step_index].element_path_type	=str(text_detail)
				elif text_type=='element_path'		:self.action_list[step_index].element_path 		=str(text_detail)
				elif text_type=='identify_flag'		:self.action_list[step_index].identify_flag 	=str(text_detail)
				elif text_type=='contents'			:self.action_list[step_index].contents			=str(text_detail)
				elif text_type=='sleep_time'		:self.action_list[step_index].sleep_time 		=int(text_detail)
				elif text_type=='goto_step'			:self.action_list[step_index].goto_step 		=str(text_detail)
				elif text_type=='reference_flag'	:self.action_list[step_index].reference_flag 	=str(text_detail)
				elif text_type=='select_type'		:self.action_list[step_index].select_type 		=str(text_detail)
				elif text_type=='return_flag'		:self.action_list[step_index].return_flag 		=str(text_detail)

	def Process_Action(self):
		step_index = 0
		while step_index < len(self.action_list):
			action=self.action_list[str(step_index)]
			step_index+=1

			if action.reference_flag=='elements':
				if action.return_flag!=self.return_flag and action.return_flag!='':
					self.return_flag=action.return_flag
					self.return_contents[action.return_flag]={}
				for element in self.elements:
					self.Do_Action(action,element)
			elif action.reference_flag=='element':
				if action.return_flag!=self.return_flag and action.return_flag!='':
					self.return_flag=action.return_flag
					self.return_contents[action.return_flag]={}
				self.Do_Action(action,self.element)
			else:
				self.Do_Action(action,self.driver)
			if action.sleep_time!='':time.sleep(action.sleep_time)

	def Do_Action(self,action,driver):
		print 'action_type:',action.action_type
		if   action.action_type=='open_page':
			Tools_Pool.open_url(action.url,driver)

		if   action.action_type=='find_element':
			self.element=Tools_Pool.get_element(action,driver)

		elif action.action_type=='find_elements':
			self.elements=Tools_Pool.get_elements(action,driver)

		elif action.action_type=='select':
			element=Tools_Pool.get_element(action,driver)
			if element:Tools_Pool.select(element,action)

		elif action.action_type=='input_text':
			element=Tools_Pool.get_element(action,driver)
			if element:Tools_Pool.element_input_text(element,action)

		elif action.action_type=='click_button':
			element=Tools_Pool.get_element(action,driver)
			if element:Tools_Pool.click_button(element)

		elif action.action_type=='click_enter':
			element=Tools_Pool.get_element(action,driver)
			if element:Tools_Pool.click_enter(element)

		elif action.action_type=='download_img':
			element=Tools_Pool.get_element(action,driver)
			if element:Tools_Pool.download_img(element,action.identify_flag)

		elif action.action_type=='download_html':
			Tools_Pool.download_html(driver)

		elif action.action_type=='get_text':
			#element=Tools_Pool.get_element(action,driver)
			if driver:Tools_Pool.get_text(driver)

		elif action.action_type=='get_attribute':
			if driver:
				Tools_Pool.get_attribute(self,driver,action)
'''
if __name__ == "__main__":
	try:
		main=Main()
		main.run()
	except:
		print traceback.print_exc()
	#main.driver.quit()
'''