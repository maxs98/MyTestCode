# -*- coding: utf-8 -*-

#/usr/bin/python

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup          # For processing HTML
from BeautifulSoup import BeautifulStoneSoup     # For processing XML
import BeautifulSoup                             # To get everything

url = 'http://blog.csdn.net/s98/article/details/7279084'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
'location' : 'Northampton',
'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
webcontext = response.read()
soup = BeautifulSoup.BeautifulStoneSoup(webcontext)
print soup.body.next
''' #divtag = soup.find('div',id="article_content")
divtag = soup.find('div',{"class":"article_content"})
for my in divtag:
	for aaa in my.p.contents:
		print aaa
		#divtag.next
print len(divtag.contents)
 #print divtag.p.string'''



    


