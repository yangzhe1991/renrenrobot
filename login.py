import urllib
import urllib2
import cookielib
import sys
from StringIO import StringIO
def login():
	xn={}
	xn['email']='youknow'
	xn['password']='you ye know'
	cookie=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	urllib2.install_opener(opener)
	zhanghao = urllib.urlencode(xn)
	req=urllib2.Request('http://3g.renren.com/login.do?fx=0&autoLogin=true',zhanghao)
	resp=urllib2.urlopen(req)
	return resp.read()
