import urllib
path = "http://xuanke.tongji.edu.cn/CheckImage"

import threading  
import time
class total(threading.Thread):
	def __init__(self,num,time):
		threading.Thread.__init__(self)  
		self.num=num
		self.time=time
	def run(self):
		for i in range(0,self.num):
			time.sleep(self.time)
			t=mythread(path,"temp3\\"+str(i)+".gif")
			t.start()
class mythread(threading.Thread):  
	def __init__(self,path,file):  
		threading.Thread.__init__(self)  
		self.path = path 
		self.file=file
	def run(self):
		urllib.urlretrieve(self.path, self.file) 


t=total(500,0.2)
t.start()
#t=mythread(path,"temp3\\"+str(5)+".gif")
#t.start()
#	urllib.urlretrieve(path, "temp3\\"+str(i)+".gif") 
#	thread.start_new_thread(download,(path, "temp3\\"+str(i)+".gif") )

	
	
	