import sys
import traceback
sys.path.append('E:\\Web_Script_Tools')
import main_logic

class test1():
	id_=''
	name_=''
	class test2():
		id_=''
		name_=''

a={}
a['name']=['a','b','c']
a['id']=['1','2','3']

b={}
b['name']=['aa','bb','cc']
b['id']=['11','22','33']
print a
test={}
for index in range(0,len(a['id'])):
	test[index]=test1()
test[0].test2={}
for index in range(0,10):
	test[0].test2[index]=test1.test2()
	test[0].test2[index].id_=index

for index in test[0].test2:
	print index,test[0].test2[index].id_

