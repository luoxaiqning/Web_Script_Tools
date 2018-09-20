import main_logic
import sys
reload(sys)  
sys.setdefaultencoding('utf8') 

run=main_logic.Main()
run.Get_Action_List()
print run.Process_Action()