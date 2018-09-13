import urllib
'''
url='http://chromedriver.storage.googleapis.com/2.40/chromedriver_win32.zip'
name=url.split('.')[-2].split('/')[-1]+'.'+url.split('.')[-1]
print name
urllib.urlretrieve(url,name)
'''
file=open('test.txt','w')
file.write('test')
file.close()