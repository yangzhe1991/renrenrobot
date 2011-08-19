# coding=utf-8
import urllib
import urllib2
import cookielib
import sys
import poststatus
import time
import login
from StringIO import StringIO


def zhuanfa():
	html=login.login()	
	index=html.find('写日志')
	html=html[index:]
	index=html.find('转自')
	#print html
	while index>=0:
		time.sleep(3)
		html=html[index:]
		index2=html.find('<br')
		sss=html[:index2]
		html=html[index2:]
		html=html[html.find(':'):]
		sss+=html[:html.find('</p>')]
		html=html[html.find('</p>')+3:]
		fw=open('zhuanfa.db','a')
		fr=open('zhuanfa.db','r')
		alllines=fr.readlines()
		sss=str(sss)
		if sss.find('杨哲')>=0:
			index=html.find('转自')
			continue
		i=sss.find('<im')
		while i>=0:
			j=sss.find('/>')
			sss=sss.replace(sss[i:j+2],'')
			i=sss.find('<im')
		fr.close()
		boo=1
		for each in alllines:
			if sss.find(each[len(each)/2:len(each)/3*2])>0:
				boo=0
		if boo==1:
			poststatus.zhuangtai('自动转发:'+sss)
			fw.write('\n'+sss+'\n')
			#print '\n已存'+sss
		else:
			pass			
			#print '发现转发过的状态'
		index=html.find('转自')
