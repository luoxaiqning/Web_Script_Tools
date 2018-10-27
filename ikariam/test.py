import time

switch='on'


while switch=='on':
	time.sleep(1)
	file=open('switch.txt','r')
	switch=file.read()
	file.close()
	print time.localtime()
	if time.localtime().tm_sec==5:
		print 'mark'