from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import traceback

def get_text(element):
	try:
		print 'element.text',element.text
	except:
		pass

def download_img(element,flag):
	try:
		import urllib
		img_url=element.get_attribute('src')
		if flag=='jandan':
			img_url=img_url.replace('thumb180','large')
		print img_url
			
		name='img/'+img_url.split('.')[-2].split('/')[-1]+'.'+img_url.split('.')[-1]
		urllib.urlretrieve(img_url,name)
	except:
		pass

def download_html(driver):
	html=driver.execute_script("return document.documentElement.outerHTML")
	file=open('html.html','w')
	file.write(html)
	file.close()
'''
def print_element(element):
	print element.get_attribute('innerHTML')
	self.return_contents[action.return_flag][len(self.return_contents[action.return_flag])]=element.get_attribute('innerHTML')
'''
def set_attribute(self,driver,element,action):
	driver.execute_script("arguments[0].setAttribute("+action.contents+")",element)

def get_attribute(self,element,action):
	#print 'mark',action.return_flag,len(self.return_contents[action.return_flag])
	self.return_contents[action.return_flag][len(self.return_contents[action.return_flag])]=element.get_attribute(action.contents)

def click_button(element):
	#print element.get_attribute('id')
	element.click()

def click_enter(element):
	element.send_keys(Keys.ENTER)

def element_input_text(element,action):
	#print 'action.contents',action.contents
	#print 'element',element
	#print element.get_attribute('class')
	element.send_keys(action.contents.decode('utf8'))

def select(element,action):
	from selenium.webdriver.support.select import Select
	if   action.select_type=='by_index':
		Select(element).select_by_index(action.contents)
	elif action.select_type=='by_value':
		Select(element).select_by_value(action.contents)
	elif action.select_type=='by_text':
		Select(element).select_by_visible_text(action.contents)

def get_element(action,driver):
	try:
		if   action.element_path_type=='by_id':
			element=driver.find_element_by_id(action.element_path)
		elif action.element_path_type=='by_class':
			element=driver.find_element_by_class_name(action.element_path)
		elif action.element_path_type=='by_xpath':
			element=driver.find_element_by_xpath(action.element_path)
		elif action.element_path_type=='by_tag':
			element=driver.find_element_by_tag_name(action.element_path)
		elif action.element_path_type=='by_text':
			element=driver.find_element_by_link_text(action.element_path)
		elif action.element_path_type=='by_jQuery':
			element=driver.execute_script(action.element_path)
		
	except:
		#print traceback.print_exc()
		print 'Unable to locate element'
		return False
	return element

def get_elements(action,driver):
	try:
		if   action.element_path_type=='by_id':
			elements=driver.find_elements_by_id(action.element_path)
		elif action.element_path_type=='by_class':
			elements=driver.find_elements_by_class_name(action.element_path)
		elif action.element_path_type=='by_xpath':
			elements=driver.find_elements_by_xpath(action.element_path)
		elif action.element_path_type=='by_tag':
			elements=driver.find_elements_by_tag_name(action.element_path)
		elif action.element_path_type=='by_text':
			elements=driver.find_elements_by_link_text(action.element_path)
		elif action.element_path_type=='by_jQuery':
			elements=driver.execute_script(action.element_path)
	except:
		#print traceback.print_exc()
		print 'Unable to locate element'
		return False
	return elements

def open_url(url,driver):
	try:
		print url
		driver.get(url)
	except TimeoutException:
		print 'page stop'

