import re
import Initialize_logic

def Get_Planet_List(html):
	html = html.replace(" ","").replace("\n","").replace("\t","")
	for planets in re.compile(r'id="planet-.*?</a>').findall(html):
		name   = re.compile(r'planet-name">[^<]*').search(planets).group().replace('planet-name">','')
		id_    = re.compile(r'id="planet-\d*').search(planets).group().replace('id="planet-','')
		koords = re.compile(r'planet-koords">[^<]*').search(planets).group().replace('planet-koords">','')
		Initialize_logic.Global_.planet_id[name] 	 = id_
		Initialize_logic.Global_.planet_koords[name] = koords
	return True

def Get_Planet_Resources(html,text):
	text = text.replace(" ","")
	html = html.replace(" ","").replace("\n","").replace("\t","").replace(".","").replace("\"","")
	res_number = re.compile(text+'.*?</span>').search(html).group()
	res_number = re.compile(r'\d\d*|-\d\d*').search(res_number).group()
	return res_number

def Get_Planet_Building_Level(html,text):
	text = text.replace(" ","")
	html = html.replace(" ","").replace("\n","").replace("\t","").replace(".","").replace("\"","")
	building_level = re.compile(text+'</span>\d.*?</a>').search(html)
	if building_level:
		building_level = re.compile(r'\d\d*').search(building_level.group()).group()
		return building_level
	return 'In construction'

def Get_Planet_In_Construction(html):
	html = html.replace("\n","").replace("\t","").replace(".","").replace("\"","")
	in_construction = re.compile(r'Nobuildingsinconstruction').search(html)
	if in_construction:
		return 'No buildings in construction'
	in_construction = re.compile(r'Cancelexpansionof.*?\d+').search(html).group().replace("Cancelexpansionof","")
	return in_construction

def Get_Building_Upgrade_Url(html,text):
	text = text.replace(" ","")
	html = html.replace(" ","").replace("\n","").replace("\t","").replace("\'","")
	Building_type = re.compile('title="'+text+'.*?'+text).search(html).group()
	Building_type = re.compile(r'\d+').search(Building_type).group()
	Building_Upgrade_Url = re.compile(r'sendBuildRequest\(https://s150-en\.ogame\.gameforge\.com/game/index\.php\?page=(resources|station)&modus=1&type='+str(Building_type)+'.*?<imgsrc').search(html)
	if Building_Upgrade_Url:
		Building_Upgrade_Url = re.compile(r'https.*,null').search(Building_Upgrade_Url.group()).group().replace(",null","")
		return Building_Upgrade_Url
	else:
		return False

def Get_Planet_Fleet(html,text):
	text = text.replace(" ","")
	html = html.replace(" ","").replace("\n","").replace("\t","").replace("\'","")
	number = re.compile(r'<spanclass="textlabel">'+text+'.*?</a>|title="'+text+'.*?\)').search(html).group()
	number = re.compile(r'\d\d*').search(number).group()
	return number

def Get_Planet_Defense(html,text):
	text = text.replace(" ","")
	html = html.replace(" ","").replace("\n","").replace("\t","").replace("\'","")
	number = re.compile(r'<spanclass="textlabel">'+text+'.*?</a>|title="'+text+'.*?\)').search(html).group()
	number = re.compile(r'\d\d*').search(number).group()
	return number

def Get_Planet_In_Production(html,text):
	number = 0
	in_queue = 0
	text = text.replace(" ","")
	html = html.replace(" ","").replace("\n","").replace("\t","").replace("\'","")
	try:
		in_production = re.compile(r'Productionof.*?'+text+'inprogress').search(html).group()
		in_production = int(re.compile(r'\d\d*').search(in_production).group())
	except:
		in_production = 0
	try:
		in_queue_list = re.compile(r'Productionqueue.*<!--ENDCONTENTAREA-->').search(html).group()
		in_queue_list = re.compile(r'title=".*?'+text).findall(in_queue_list)
		for queue in in_queue_list:
			in_queue = in_queue + int(re.compile(r'\d\d*').search(queue).group())
	except:
		in_queue = 0
	number = in_production + in_queue
	return number

def Get_Data(html):
	data = re.compile(r'\d+').search(html).group()
	return int(data)

def Get_Match(html,text):
	if re.compile(text).search(html):
		return True
	return False

def Get_Token(html):
	html = html.replace(" ","").replace("\n","").replace("\t","").replace("\'","")
	token = re.compile(r'tokenvalue=.*?/>').search(html).group()
	token = token.replace("tokenvalue=","").replace("/>","")
	return token

def Get_Target_list(html):
	html  = html.replace("\n","").replace("\t","").replace("\'","").replace("\"","").replace("Mn","000").replace('&nbsp;','')
	messages = re.compile(r'class=msg_content.{1500}').findall(html)
	target_list={}
	int_=0
	for message in messages:
		try:
			player = re.compile(r'Player:.{400}').search(message).group()
			status = re.compile(r'abbr_.*?>').search(player).group().replace('abbr_','').replace('>','')
			player = player.replace('Player:</span><span class=status_abbr','')
			player = re.compile(r'[^>]*</span><span class=status_abbr').search(player).group().replace('</span><span class=status_abbr','')
		except:
			pass
		try:
			url = re.compile(r'https://s\d*-en\.ogame\.gameforge\.com/game/index\.php\?page=fleet1\&amp\;galaxy=\d*&amp;system=\d*\&amp\;position=\d*\&amp\;type=1\&amp\;mission=1\&amp\;am202=\d*').search(message).group().replace('amp;','')
		except:
			continue
		try:
			resources= Get_Data(re.compile(r'Resources: [\d|.]*').search(message).group().replace(".",""))
		except:
			resources= 0
		try:
			fleets   = Get_Data(re.compile(r'Fleets: [\d|.]*').search(message).group().replace(".",""))
		except:
			fleets   = 999999999
		try:
			defence  = Get_Data(re.compile(r'Defence: [\d|.]*').search(message).group().replace(".",""))
		except:
			defence  = 999999999
		try:
			kroods   = re.compile(r'galaxy.*type').search(url).group()
			kroods   = re.compile(r'\d\d*').findall(kroods)
		except:
			pass
		target_list[int_]= {'':''}
		target_list[int_]['Player']=player
		target_list[int_]['Status']=status
		target_list[int_]['Resources'] = resources
		target_list[int_]['Fleets']=fleets
		target_list[int_]['Defence']=defence
		target_list[int_]['Url']=url
		target_list[int_]['Koords']=kroods
		int_ += 1
	return target_list

html='<span class="msg_content"><br /><br /><div class="compacting"><span class="ctn ctn4">Player:</span><span class="status_abbr_longinactive"> <span class="honorRank rank_starlord3 tooltip" title="Star Lord"> </span> wolfhound</span><span class="status_abbr_inactive">(<span class="status_abbr_inactive"><span class="status_abbr_inactive tooltip js_hideTipOnMobile" title="7 days inactive">i</span></span>)</span> <span class="ctn ctn4 fright"><font color="#FF0000">Activity: &lt;15 minutes ago.</font></span></div><div class="compacting"><span class="ctn ctn4"><span class="resspan">Metal: 573.989</span><span class="resspan">Crystal: 336.638</span><span class="resspan">Deuterium: 75.891</span></span><span class="ctn ctn4 fright tooltipRight tooltipClose" title="Loot: 493.259&lt;br/&gt;&lt;a href=&quot;https://s145-en.ogame.gameforge.com/game/index.php?page=fleet1&amp;galaxy=1&amp;system=1&amp;position=15&amp;type=1&amp;mission=1&amp;am202=99&quot;&gt;S.Cargo: 99&lt;/a&gt;&lt;br/&gt;&lt;a href=&quot;https://s145-en.ogame.gameforge.com/game/index.php?page=fleet1&amp;galaxy=1&amp;system=1&amp;position=15&amp;type=1&amp;mission=1&amp;am203=20&quot;&gt;L.Cargo: 20&lt;/a&gt;&lt;br/&gt;">Resources: 986.518</span></div><div class="compacting"><span class="ctn ctn4">Loot: 50%</span><span class="fright">Chance of counter-espionage: 0%</span></div><div class="compacting"> <span class="ctn ctn4 tooltipLeft" title="Fleets: 0">Fleets: 0</span>  <span class="ctn ctn4 fright tooltipRight" title="0">Defence: 0</span></div><br />XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\
        <span class="msg_content"><br /><br /><div class="compacting"><span class="ctn ctn4">Player:</span><span class="status_abbr_honorableTarget"> <span class="honorRank rank_starlord3 tooltip" title="Star Lord"> </span> Starz</span><span class="status_abbr_active"></span> <span class="ctn ctn4 fright">Activity: &gt;60 minutes ago.</span></div><div class="compacting"><span class="ctn ctn4"><span class="resspan">Metal: 41.286</span><span class="resspan">Crystal: 29.876</span><span class="resspan">Deuterium: 22.715</span></span><span class="ctn ctn4 fright tooltipRight tooltipClose" title="Loot: 70.407&lt;br/&gt;&lt;a href=&quot;https://s150-en.ogame.gameforge.com/game/index.php?page=fleet1&amp;galaxy=3&amp;system=221&amp;position=9&amp;type=1&amp;mission=1&amp;am202=15&quot;&gt;S.Cargo: 15&lt;/a&gt;&lt;br/&gt;&lt;a href=&quot;https://s150-en.ogame.gameforge.com/game/index.php?page=fleet1&amp;galaxy=3&amp;system=221&amp;position=9&amp;type=1&amp;mission=1&amp;am203=3&quot;&gt;L.Cargo: 3&lt;/a&gt;&lt;br/&gt;">Resources: 93.877</span></div><div class="compacting"><span class="ctn ctn4">Loot: 75%</span><span class="fright">Chance of counter-espionage: 0%</span></div><div class="compacting"></div><br />XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx\
<span class="msg_content"><br /><br /><div class="compacting"><span class="ctn ctn4">Player:</span><span class="status_abbr_honorableTarget"> <span class="honorRank rank_bandit1 tooltipHTML" title="Bandit King|All battles against bandits are honourable, which means they never flee!&lt;br /&gt;&lt;br /&gt; Their planets are not protected from plundering."> </span> Gorestone</span><span class="status_abbr_active">(<span class="status_abbr_bandit"></span>)</span> <span class="ctn ctn4 fright">Activity: &gt;60 minutes ago.</span></div><div class="compacting"><span class="ctn ctn4"><span class="resspan">Metal: 481.041</span><span class="resspan">Crystal: 250.097</span><span class="resspan">Deuterium: 136.784</span></span><span class="ctn ctn4 fright tooltipRight tooltipClose" title="Loot: 867.922&lt;br/&gt;&lt;a href=&quot;https://s150-en.ogame.gameforge.com/game/index.php?page=fleet1&amp;galaxy=3&amp;system=243&amp;position=9&amp;type=1&amp;mission=1&amp;am202=174&quot;&gt;S.Cargo: 174&lt;/a&gt;&lt;br/&gt;&lt;a href=&quot;https://s150-en.ogame.gameforge.com/game/index.php?page=fleet1&amp;galaxy=3&amp;system=243&amp;position=9&amp;type=1&amp;mission=1&amp;am203=35&quot;&gt;L.Cargo: 35&lt;/a&gt;&lt;br/&gt;">Resources: 867.922</span></div><div class="compacting"><span class="ctn ctn4">Loot: 100%</span><span class="fright">Chance of counter-espionage: 100%</span></div><div class="compacting"></div><br />XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#print Get_Target_list(html)



def Get_Fleet_Line(html):
	html  = html.replace(" ","").replace("\n","").replace("\t","").replace("\'","").replace("\"","")
	html  = re.compile(r'Fleets:.*?</div>').search(html).group()
	lines = re.compile(r'\d\d*').findall(html)
	if lines[0] == lines[1]:
		return False,0
	else:
		return True,int(lines[1])-int(lines[0])
