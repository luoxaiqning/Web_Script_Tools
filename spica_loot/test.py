
def load_setup():
		file = open('Setup.txt','r')
		text = file.readlines()
		ser_id   				= str(text[0].split(':')[1]).replace('\n','')
		username 				= str(text[1].split(':')[1])
		password 				= str(text[2].split(':')[1])
		time_relogin 			= str(text[3].split(':')[1])
		time_get_fleet_line		= str(text[4].split(':')[1])
		time_esp_low 			= str(text[5].split(':')[1])
		time_esp_top 			= str(text[6].split(':')[1])
		time_analyze_message 	= str(text[7].split(':')[1])
		loot_resources_trigger 	= str(text[8].split(':')[1])
		loot_defence_trigeer 	= str(text[9].split(':')[1])
		loot_galaxy_from 		= str(text[10].split(':')[1])
		loot_galaxy_to 			= str(text[11].split(':')[1])
		print ser_id
		print '11111'+ser_id+'2222'

load_setup()
a= 3
print 10/int(a)