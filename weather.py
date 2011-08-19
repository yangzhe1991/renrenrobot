# coding=utf-8
import urllib

def tomorrow(city):
	html=urllib.urlopen('http://3g.sina.com.cn/prog/wapsite/weather_new/forecast_new.php?city='+city+'&vt=4').read();
	i0=html.find('明天')
	html=html[i0:]
	l1=html.find('白天')
	html=html[l1:]
	sss='明天白天 '
	l2=html.find('/>')+2
	html=html[l2:]
	l3=html.find('<b')
	sss+=html[:l3]+'。'
	#print l2,l3
	l1=html.find('夜间')
	html=html[l1:]
	sss+='明天夜间 '
	l2=html.find('/>')+2
	html=html[l2:]
	l3=html.find('<b')
	sss+=html[:l3]+'。'
	return '下面发布明天'+city+'天气：'+sss

def today(city):
	html=urllib.urlopen('http://3g.sina.com.cn/prog/wapsite/weather_new/forecast_new.php?city='+city+'&vt=4').read();


def now():
	html=urllib.urlopen('http://3g.sina.com.cn/prog/wapsite/weather_new/airport_cities.php?city=%C9%F2%D1%F4&cf=c&vt=4').read();
	l=html.find('沈阳桃仙机场')
	html=html[l:]
	l=html.find('&nbs')
	html=html[l:]
	l=html.find(';')+1
	r=html.find('<b')
	return '下面发布当前沈阳天气：'+html[l:r]


