# coding: utf-8
import time
import random
import traceback
import Tools_Pool
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
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
	element 			=''
	elements 			=''
	reference_element   =''
	url 				=''
	identify_flag 		=''
	
		

class Main():
	def __init__(self):
		firefoxProfile=FirefoxProfile() 								# 	
		#firefoxProfile.set_preference('permissions.default.image',2)	# 
		#self.driver=webdriver.Firefox(firefoxProfile)
		chrome_options=Options()
		chrome_options.add_argument('--headless')
		self.driver=webdriver.Chrome(chrome_options=chrome_options)
		#self.driver=webdriver.Chrome()
		self.driver.set_page_load_timeout(20)
		#self.driver.set_window_size(500,500)

	
	def run(self):
		try:
			self.Get_Action_List()
			self.Process_Action()
			self.driver.quit()
			print 'end'
		except:
			self.driver.quit()
			print 'error'
			print traceback.print_exc()


	def Get_Action_List(self):
		file = open('Action_List1.csv','r')
		text = file.readlines()
		file.close()
		self.action_list={}

		for action_step in text[1:]:
			step_index   	 =int(action_step.split(',')[0].replace('\n',''))
			action_type 	 =action_step.split(',')[1].replace('\n','')
			element_path_type=action_step.split(',')[2].replace('\n','')
			element_path 	 =action_step.split(',')[3].replace('\n','')
			contents 	 	 =action_step.split(',')[4].replace('\n','')[1:]
			sleep_time 	 	 =action_step.split(',')[5].replace('\n','')
			if sleep_time=='':sleep_time=int(1)
			else:sleep_time=int(sleep_time)
			goto_step 	 	 =action_step.split(',')[6].replace('\n','')
			reference_element=action_step.split(',')[7].replace('\n','')

			self.action_list[step_index]=Action_List()
			self.action_list[step_index].action_type   	  =action_type
			self.action_list[step_index].element_path_type=element_path_type
			self.action_list[step_index].element_path 	  =element_path
			self.action_list[step_index].contents 	 	  =contents
			self.action_list[step_index].sleep_time       =sleep_time
			self.action_list[step_index].goto_step 	      =goto_step
			self.action_list[step_index].reference_element=reference_element

	def Process_Action(self):
		step_index = 0
		while step_index < len(self.action_list):
			action=self.action_list[step_index]
			step_index+=1

			#判断是操纵的全局还是局部的元素，在判断中分别赋予对应的元素
			if action.reference_element=='':
				#如果是在全局，则直接执行操作
				self.Do_Action(action,self.driver)
			else:
				#如果是在之前抓取的元素中执行进一步操作，则首先判断是元素还是元素组
				if   self.action_list[int(action.reference_element)].action_type=='find_element':
					#是元素则直接执行操作
					element =self.action_list[int(action.reference_element)].element
					self.Do_Action(action,element)
				elif self.action_list[int(action.reference_element)].action_type=='find_elements':
					#是元素组则需要对全部元素进行循环执行
					elements=self.action_list[int(action.reference_element)].elements
					for element in elements:
						self.Do_Action(action,element)
				else:
					#没有输入相关元素步骤
					print 'error'

			time.sleep(action.sleep_time)

	def Do_Action(self,action,driver):
		print 'action_type:',action.action_type
		if   action.action_type=='open_page':
			Tools_Pool.open_url(action,driver)

		if   action.action_type=='find_element':
			action.element=Tools_Pool.get_element(action,driver)

		if   action.action_type=='find_elements':
			action.elements=Tools_Pool.get_elements(action,driver)

		elif action.action_type=='input_text':
			action.element=Tools_Pool.get_element(action,driver)
			Tools_Pool.element_input_text(action)

		elif action.action_type=='click_button':
			action.element=Tools_Pool.get_element(action,driver)
			Tools_Pool.click_button()

		elif action.action_type=='download_img':
			action.element=Tools_Pool.get_element(action,driver)
			Tools_Pool.download_img(action.element,action.contents)

		elif action.action_type=='download_html':
			Tools_Pool.download_html(driver)

		elif action.action_type=='download_text':
			action.element=Tools_Pool.get_element(action,driver)
			Tools_Pool.download_text(action.element)



if __name__ == "__main__":
	main=Main()
	main.run()
