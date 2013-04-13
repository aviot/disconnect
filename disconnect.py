# -*- coding: utf-8 -*-
import os,time
# call rasdial disconnect connect.
os.system('rasdial /Disconnect')
# call rasdial connect entyname account passport.
result = os.system('rasdial entyname account passport')
# if connect failed ,wait 10 second and retry 10 times.
count = 10
while result == 0 and count >0:
	time.sleep(10)
	result=os.system('rasdial enty account passport')
	count -= 1
