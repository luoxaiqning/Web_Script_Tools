import sys
sys.path.append('E:\\Web_Script_Tools')
import main_logic
main=main_logic.Main()
main.Get_Action_List('test')
main.Process_Action()
contents=main.return_contents
main.driver.quit()
for index in contents['test2']:
	print contents['test2'][index]
