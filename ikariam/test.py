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
chrome_options=Options()
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('E:\\Web_Script_Tools\\ikariam\\html.html')

element=driver.find_element_by_xpath("//a[contains(@title,'qing2')]")
print element
print element.get_attribute('title')
print element.get_attribute('href')
driver.quit()