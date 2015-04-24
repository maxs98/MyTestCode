#!/usr/bin/python
#coding=utf-8

import requests

browse_headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
keyword = raw_input("keywords:")
s = requests.Session()
url = "http://fanyi.youdao.com/openapi.do?keyfrom=maxs98&key=1081121042&type=data&doctype=json&version=1.1&q=%s"%keyword
html = s.get(url,headers=browse_headers)
data = html.json()
translation = data['translation']
translation = translation.pop().encode('utf-8')
print translation
print "====================="
web = data['web']
print type(web[0])
print "------------"
print web[0].values()
print "------------"
#print web[0].values()[1]
for i in web[0].values()[1]:
	print i
'''
for k in web[0].items():
	#print k
	for i in k:
		print i
#print html.json()
'''
