class Action_List():
	action_type		=''
	element_path_type 	=''
	element_path 	=''
	contents  		=''
	sleep_time 		=''
	goto_step 		=''
def Get_Action_List():
		file = open('Action_List.csv','r')
		text = file.readlines()
		file.close()
		action_list={}

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

			action_list[step_index]=Action_List()
			action_list[step_index].action_type =action_type
			action_list[step_index].element_path_type=element_path_type
			action_list[step_index].element_path=element_path
			action_list[step_index].contents 	 =contents
			action_list[step_index].sleep_time  =sleep_time
			action_list[step_index].goto_step 	 =goto_step

		return action_list
Action_List=Get_Action_List()
for index in Action_List:
	Action=Action_List[int(index)]
	print Action.contents.decode('utf8')