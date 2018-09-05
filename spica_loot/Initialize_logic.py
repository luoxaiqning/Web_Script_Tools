# -*- coding: utf-8 -*-
class Global_():
	planet_id	 	={}
	planet_koords	={}
	planet_resources={}
	planet_building_level={}
	planet_fleet	={}
	planet_defense	={}
	
	subject_ref = {}
	subject_ref['Metal Mine']			= 1
	subject_ref['Crystal Mine']			= 2
	subject_ref['Deuterium Synthesizer']= 3
	subject_ref['Solar Plant']			= 4
	subject_ref['Fusion Reactor']		= 12
	subject_ref['Metal Storage']		= 22
	subject_ref['Crystal Storage']		= 23
	subject_ref['Deuterium Tank']		= 24
	subject_ref['Robotics Factory']		= 14
	subject_ref['Shipyard']				= 21
	subject_ref['Research Lab']			= 31
	subject_ref['Alliance Depot']		= 34
	subject_ref['Missile Silo']			= 44
	subject_ref['Nanite Factory']		= 15
	subject_ref['Terraformer']			= 33
	subject_ref['Space Dock']			= 36
	subject_ref['Light Fighter']		= 204
	subject_ref['Heavy Fighter']		= 205
	subject_ref['Cruiser']				= 206
	subject_ref['Battleship']			= 207
	subject_ref['Battlecruiser']		= 215
	subject_ref['Bomber']				= 211
	subject_ref['Destroyer']			= 213
	subject_ref['Deathstar']			= 214
	subject_ref['Small Cargo']			= 202
	subject_ref['Large Cargo']			= 203
	subject_ref['Colony Ship']			= 208
	subject_ref['Recycler']				= 209
	subject_ref['Espionage Probe']		= 210
	subject_ref['Solar Satellite']		= 212
	subject_ref['Rocket Launcher']		= 401
	subject_ref['Light Laser']			= 402
	subject_ref['Heavy Laser']			= 403
	subject_ref['Gauss Cannon']			= 404
	subject_ref['Ion Cannon']			= 405
	subject_ref['Plasma Turret']		= 406
	subject_ref['Small Shield Dome']	= 407
	subject_ref['Large Shield Dome']	= 408
	subject_ref['Anti-Ballistic Missiles']	= 502
	subject_ref['Interplanetary Missiles']	= 503

	subject_order = {}
	subject_order[10] ='Metal'
	subject_order[20] ='Crystal'
	subject_order[30] ='Deuterium'
	subject_order[40] ='Energy'
	subject_order[50] ='Darkmatter'
	subject_order[101]='Metal Mine'
	subject_order[102]='Crystal Mine'
	subject_order[103]='Deuterium Synthesizer'
	subject_order[104]='Solar Plant'
	subject_order[105]='Fusion Reactor'
	subject_order[106]='Metal Storage'
	subject_order[107]='Crystal Storage'
	subject_order[108]='Deuterium Tank'
	subject_order[201]='Robotics Factory'
	subject_order[202]='Shipyard'
	subject_order[203]='Research Lab'
	subject_order[204]='Alliance Depot'
	subject_order[205]='Missile Silo'
	subject_order[206]='Nanite Factory'
	subject_order[207]='Terraformer'
	subject_order[208]='Space Dock'
	subject_order[299]='In Construction'
	subject_order[301]='Light Fighter'
	subject_order[302]='Heavy Fighter'
	subject_order[303]='Cruiser'
	subject_order[304]='Battleship'
	subject_order[305]='Battlecruiser'
	subject_order[306]='Bomber'
	subject_order[307]='Destroyer'
	subject_order[308]='Deathstar'
	subject_order[309]='Small Cargo'
	subject_order[310]='Large Cargo'
	subject_order[311]='Colony Ship'
	subject_order[312]='Recycler'
	subject_order[313]='Espionage Probe'
	subject_order[314]='Solar Satellite'
	subject_order[401]='Rocket Launcher'
	subject_order[402]='Light Laser'
	subject_order[403]='Heavy Laser'
	subject_order[404]='Gauss Cannon'
	subject_order[405]='Ion Cannon'
	subject_order[406]='Plasma Turret'
	subject_order[407]='Small Shield Dome'
	subject_order[408]='Large Shield Dome'
	subject_order[409]='Anti-Ballistic Missiles'
	subject_order[410]='Interplanetary Missiles'
		
	subject_type = {}
	subject_type['Metal Mine']				= 'resources'
	subject_type['Crystal Mine']			= 'resources'
	subject_type['Deuterium Synthesizer']	= 'resources'
	subject_type['Solar Plant']				= 'resources'
	subject_type['Fusion Reactor']			= 'resources'
	subject_type['Metal Storage']			= 'resources'
	subject_type['Crystal Storage']			= 'resources'
	subject_type['Deuterium Tank']			= 'resources'
	subject_type['Robotics Factory']		= 'station'
	subject_type['Shipyard']				= 'station'
	subject_type['Research Lab']			= 'station'
	subject_type['Alliance Depot']			= 'station'
	subject_type['Missile Silo']			= 'station'
	subject_type['Nanite Factory']			= 'station'
	subject_type['Terraformer']				= 'station'
	subject_type['Space Dock']				= 'station'
	subject_type['In Construction']			= ''
	subject_type['Light Fighter']			= 'shipyard'
	subject_type['Heavy Fighter']			= 'shipyard'
	subject_type['Cruiser']					= 'shipyard'
	subject_type['Battleship']				= 'shipyard'
	subject_type['Battlecruiser']			= 'shipyard'
	subject_type['Bomber']					= 'shipyard'
	subject_type['Destroyer']				= 'shipyard'
	subject_type['Deathstar']				= 'shipyard'
	subject_type['Small Cargo']				= 'shipyard'
	subject_type['Large Cargo']				= 'shipyard'
	subject_type['Colony Ship']				= 'shipyard'
	subject_type['Recycler']				= 'shipyard'
	subject_type['Espionage Probe']			= 'shipyard'
	subject_type['Solar Satellite']			= 'shipyard'
	subject_type['Rocket Launcher']			= 'defense'
	subject_type['Light Laser']				= 'defense'
	subject_type['Heavy Laser']				= 'defense'
	subject_type['Gauss Cannon']			= 'defense'
	subject_type['Ion Cannon']				= 'defense'
	subject_type['Plasma Turret']			= 'defense'
	subject_type['Small Shield Dome']		= 'defense'
	subject_type['Large Shield Dome']		= 'defense'
	subject_type['Anti-Ballistic Missiles']	= 'defense'
	subject_type['Interplanetary Missiles']	= 'defense'


def Get_Piont_To_Construction_List():
	point_to_construction_list = {}
	point_to_construction_list[0] = {'Planet':'Homeworld','Building':'Solar Plant'   ,'Level':20}
	point_to_construction_list[1] = {'Planet':'Homeworld','Building':'Shipyard'	  	 ,'Level':8 }
	point_to_construction_list[2] = {'Planet':'Homeworld','Building':'Crystal Mine'  ,'Level':19}
	point_to_construction_list[3] = {'Planet':'Homeworld','Building':'Fusion Reactor','Level':5 }
	point_to_construction_list[4] = {'Planet':'Homeworld','Building':'Metal Mine'	 ,'Level':20 }
	return point_to_construction_list

def Get_Piont_To_Production_List():
	point_to_production_list = {}
	point_to_production_list[0] = {'Planet':'Homeworld','Subject':'Solar Satellite','Number':30}
	point_to_production_list[1] = {'Planet':'Homeworld','Subject':'Light Laser'    ,'Number':200}
	point_to_production_list[2] = {'Planet':'Homeworld','Subject':'Large Shield Dome'    ,'Number':1}
	point_to_production_list[3] = {'Planet':'Homeworld','Subject':'Rocket Launcher'    ,'Number':100}
	point_to_production_list[4] = {'Planet':'Homeworld','Subject':'Espionage Probe'    ,'Number':20}
	point_to_production_list[5] = {'Planet':'Homeworld','Subject':'Large Cargo'    ,'Number':20}
	return point_to_production_list

'''
point_to_build_list = Get_Piont_To_Build_List()
for list_ in point_to_build_list:
	planet   = point_to_build_list[list_]['Planet']
	building = point_to_build_list[list_]['Building']
	level	 = point_to_build_list[list_]['Level']
	type_	 = Global_.subject_type[building]
	print planet,building,level,type_





'''