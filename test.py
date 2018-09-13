import urllib
url='http://wx3.sinaimg.cn/mw600/8859dc85ly1fv7ox7f8czj20d80m80u8.jpg'
flag=url.split('.')
print flag[-1]
'''
img=urllib.urlopen(url).read()
f=open('test_img.jpg','wb')
f.write(img)
f.close()
'''