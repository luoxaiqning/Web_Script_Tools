import main_logic



def Get_Action_List():
	file = open('Action_List.txt','r')
	text_list = file.readlines()
	file.close()
	text_index=0
	step_index=0
	action_list={}
	for text in text_list:
		text=text.replace('\n','')
		if text!='':
			text_index,text_type,text_detail=text.replace('\t','').replace(' ','').split(',')
			if text_index>step_index:
				step_index=text_index
				action_list[step_index]=main_logic.Action_List()
			if   text_type=='action_type'	   	:action_list[step_index].action_type		=text_detail
			elif text_type=='url'				:action_list[step_index].url				=text_detail
			elif text_type=='element_path_type'	:action_list[step_index].element_path_type	=text_detail
			elif text_type=='element_path'		:action_list[step_index].element_path 		=text_detail
			elif text_type=='identify_flag'		:action_list[step_index].identify_flag 		=text_detail
			elif text_type=='contents'			:action_list[step_index].contents			=text_detail
			elif text_type=='sleep_time'		:action_list[step_index].sleep_time 		=text_detail
			elif text_type=='goto_step'			:action_list[step_index].goto_step 			=text_detail
			elif text_type=='reference_element'	:action_list[step_index].reference_element 	=text_detail
	return action_list

action_list=Get_Action_List()

for index in range(0,3):
	print index,action_list[str(index)].action_type,action_list[str(index)].url,action_list[str(index)].contents,action_list[str(index)].element_path_type