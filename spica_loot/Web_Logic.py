import time
import random
import urllib
import urllib2
import cookielib
import httplib  
import traceback
import Web_Analyze_Tools
  
httplib.HTTPConnection._http_vsn = 10  
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'  


user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
                    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'
                    ] 
cj 		= cookielib.LWPCookieJar() 
cookie_support 	= urllib2.HTTPCookieProcessor(cj)  
opener 			= urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)
user_agent = str(random.choice(user_agents))

def Get_time():
	fmt='%Y-%m-%d %H:%M:%S'
	return time.strftime(fmt,time.localtime(time.time()))

def Page_Openner(post_url,post_data):
	status = 0
	while status < 10:
		try:
			#print Get_time(),'Loading page:',post_url
			html 	= False
			headers = {
					'Referer'	:'https://en.ogame.gameforge.com/',
					'User-Agent': user_agent
					}  
			if post_data == None:
				pass
			else:
				post_data= urllib.urlencode(post_data)
			request  = urllib2.Request(post_url, post_data, headers)
			response = urllib2.urlopen(request,timeout=60)  
			html 	 = response.read()
			if html:
				return html
			status = 99
		except:
			status += 1
			#traceback.print_exc()
			print Get_time(),'Open page failed, Retry'

def Post_Fleet(planet,target,mission,fleets):
	#try:
		headers = {
					'Referer'	:'https://s150-en.ogame.gameforge.com',
					'User-Agent': user_agent
					} 
		post_url  = 'https://s150-en.ogame.gameforge.com/game/index.php?page=fleet2&cp='+str(planet)
		post_data = {	
					'type'		:1,
					'mission'	:mission,
					'galaxy'	:target['Galaxy'],
					'system'	:target['System'],
					'position'	:target['Position'],
					'speed'		:10
			        }
		for fleet in fleets:
			post_data[fleets[fleet]['Type']]=fleets[fleet]['Number']
		print 'headers',headers
		print 'post_url',post_url
		print 'post_data',post_data
		post_data = urllib.urlencode(post_data)  
		request   = urllib2.Request(post_url, post_data, headers)  
		response  = urllib2.urlopen(request,timeout=20)
		print '-------------------------------------------------'
		print response.geturl()
		#token = Web_Analyze_Tools.Get_Token(html)

		headers = {
					'Referer'	:'https://s150-en.ogame.gameforge.com/game/index.php?page=fleet2&cp='+str(planet),
					'User-Agent': user_agent
					} 
		post_url  = 'https://s150-en.ogame.gameforge.com/game/index.php?page=fleet3&cp='+str(planet)
		post_data = {	
					'type'		:1,
					'mission'	:mission,
					'union'		:0,
					'galaxy'	:target['Galaxy'],
					'system'	:target['System'],
					'position'	:target['Position'],
					'acsValues'	:'-',
					'speed'		:10
			        }
		for fleet in fleets:
			post_data[fleets[fleet]['Type']]=fleets[fleet]['Number']
		print 'headers',headers
		print 'post_url',post_url
		print 'post_data',post_data
		post_data = urllib.urlencode(post_data)  
		request   = urllib2.Request(post_url, post_data, headers)  
		response  = urllib2.urlopen(request,timeout=20)
		print '-------------------------------------------------'
		print response.geturl()
		#print response.read()

'''
		post_url  = 'https://s150-en.ogame.gameforge.com/game/index.php?page=movement&cp='+str(planet)
		post_data = {	
					'holdingtime'	:1,
					'expeditiontime':1,
					'token'			:token,
					'galaxy'		:target['Galaxy'],
					'system'		:target['System'],
					'position'		:target['Position'],
					'type'			:1,
					'mission'		:mission,
					'union2':0,
					'holdingOrExpTime':0,
					'speed'			:10,
					'acsValues'		:'-',
					'prioMetal'		:1,
					'prioCrystal'	:2,
					'prioDeuterium'	:3
			        }
			
		for fleet in fleets:
			post_data[fleets[fleet]['Type']]=fleets[fleet]['Number']
		print post_url
		print post_data
		post_data = urllib.urlencode(post_data)  
		request  = urllib2.Request(post_url, post_data, headers)  
		response = urllib2.urlopen(request,timeout=20)
		return True
	#except:
	#	pass
'''	