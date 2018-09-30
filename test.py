'''
import main_logic

driver=main_logic.Main()
driver.Get_Action_List('login.txt')
driver.Process_Action()
driver.Get_Action_List('test1.txt')
driver.Process_Action()
'''
import main_logic
driver=main_logic.Main()
driver.Get_Action_List('test1.txt')
driver.Process_Action()
for content in driver.return_contents:
	print content
