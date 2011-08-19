#!/usr/bin/python
# coding=utf-8
import poststatus
import time
import hourstatus
import thread
import getstatus
import login
import weather
#poststatus.zhuangtai('test')
def hoursleep():
	while 1==1:
		t=time.localtime(time.time()+14*3600)
		#print t[4]
		if t[4]==0:
			if t[3]<=8: 
				if t[3]==0:
					poststatus.zhuangtai('今天是'+str(t[0])+'年'+str(t[1])+'月'+str(t[2])+'日，今年的第'+str(t[7])+'天。珍惜每一天，珍惜每一个机会。')
				elif t[6]<5:
					poststatus.zhuangtai('下面是机器人打更时间：'+hourstatus.s[t[3]])
				else:
					poststatus.zhuangtai('下面是机器人打更时间：'+hourstatus.w[t[3]])
		if t[3]==22:
			if t[4]==30:
				poststatus.zhuangtai(weather.tomorrow('沈阳'))
			if t[4]==40:
				poststatus.zhuangtai(weather.tomorrow('北京'))
			if t[4]==45:
				poststatus.zhuangtai(weather.tomorrow('上海'))
			if t[4]==50:
				poststatus.zhuangtai(weather.tomorrow('本溪'))
		if t[3]==7 and t[4]==45:
			poststatus.zhuangtai(weather.now())
		if t[3]==14 and t[4]==15:
			poststatus.zhuangtai(weather.now())
		time.sleep(60)

def rtsleep():
	while 1==1:
		getstatus.zhuanfa()
		time.sleep(300)

def run():
	try:
		thread.start_new_thread(hoursleep,())
		thread.start_new_thread(rtsleep,())
	except:
		run()
login.login()

print '欢迎打开您的机器人,您可以随时输入命令。exit退出，post发任意状态,weather查询并发布天气预报'
run()
print '自动报时模块已加载'
while 1==1:
	time.sleep(600000)
