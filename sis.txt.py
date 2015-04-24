#!/usr/bin/python
#coding=utf-8

import requests
import re
import Queue
import threading
import socket

class sis001:
	def __init__(self):
		self.q = Queue.Queue(0) 
		self.s = requests.Session()
		self.browse_headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
		self.login()
		
	def login(self):
		login_info = {
		"formhash":"962ee4d3",
		"referer":"http://38.103.161.185/forum/index.php",
		"loginfield":"username",
		"62838ebfea47071969cead9d87a2f1f7":"volstad",
		"c95b1308bda0a3589f68f75d23b15938":"194105",
		"questionid":"4",
		"answer":"\xd0\xec\xc0\xf6\xbb\xaa",
		"cookietime":"2592000",
		"loginmode":"",
		"styleid":"",
		"loginsubmit":"true"}
		html = self.s.post("http://38.103.161.185/forum/logging.php?action=login&loginsubmit=true", data=login_info,headers=self.browse_headers)
		login_success_pattern = re.compile(r'volstad')
		login_success_info = login_success_pattern.search(html.content)
		if login_success_info:
			print 'login success!!'
		else:
			print 'login fail!!'

	def getTids(self):
		page = 3
		url = "http://38.103.161.185/forum/forum-62-%s.html"%page
		html = self.s.get(url,headers=self.browse_headers)
		tid_pattern = re.compile(r'<tbody id="normalthread_(\d+)\"')
		tids = tid_pattern.findall(html.content)
		#print tids
		return tids

	def getPics(self,tid):
		url = "http://38.103.161.185/forum/thread-%s-1-1.html"%tid
		html = self.s.get(url,headers=self.browse_headers)
		image_pattern = re.compile(r'\<img src\=\"(http\:\/\/.*?\.jpg|attachments\/.*?.jpg)\"')
		images = image_pattern.findall(html.content)
		images = list(set(images))
		if len(images)==0:
			print tid   #打不开的帖子
		else:
			for i in images:
				self.q.put(i)
			while True:
				if self.q.qsize()>0:
					th = threading.Thread(target=sis001.savePic)
					th.start()
					#print "Queue %s"%q.qsize()
				else:
					break
			#print images
			#return images
			
	def savePic(self):
		i = self.q.get()
		filename = re.split(r'/',i)
		fName =  '.\\img\\'+filename.pop()
		image = self.s.get(i,headers=self.browse_headers)
		open(fName, "wb").write(image.content)

if __name__ == '__main__':
	socket.setdefaulttimeout(30)
	sis001 = sis001()
	tids = sis001.getTids()
	for tid in tids:
		sis001.getPics(tid)