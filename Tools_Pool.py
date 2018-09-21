from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import traceback

def download_text(element):
	try:
		print 'element.text',element.text
	except:
		pass

def download_img(element,contents):
	try:
		import urllib
		img_url=element.get_attribute('src')
		if contents=='jandan':
			img_url=img_url.replace('thumb180','large')
		print img_url
			
		name='img/'+img_url.split('.')[-2].split('/')[-1]+'.'+img_url.split('.')[-1]
		urllib.urlretrieve(img_url,name)
	except:
		pass

def download_html(driver):
	print 'html'
	html=driver.get_attribute('innerHTML')
	print html
	#html=driver.execute_script("return document.documentElement.outerHTML")
	#file=open('test.html','w')
	#file.write(html)
	#file.close()

def click_button(element):
	element.send_keys(Keys.ENTER)
	#self.element.click()

def element_input_text(action,driver):
	print 'action.contents',action.contents
	driver.send_keys(action.contents.decode('utf8'))

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
		elif action.element_path_type=='by_jQuery':
			element=driver.execute_script(action.element_path)
	except:
		#print traceback.print_exc()
		return
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
		elif action.element_path_type=='by_jQuery':
			elements=driver.execute_script(action.element_path)
	except:
		print traceback.print_exc()
		return
	return elements

def open_url(action,driver):
	try:
		driver.get(action.contents)
	except TimeoutException:
		print 'page stop'