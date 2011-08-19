# coding=utf-8
import urllib
import urllib2
import cookielib
import sys
from StringIO import StringIO
import login
#print resp.read()
def zhuangtai(sss):
	html=login.login()
	xn2={}
	xn2['status']=sss
	xn2['update']="发布"
	zhuangtai=urllib.urlencode(xn2)
	req2=urllib2.Request('http://3g.renren.com/status/wUpdateStatus.do',zhuangtai)
	resp2=urllib2.urlopen(req2)
	print sss
