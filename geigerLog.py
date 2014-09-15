#!/usr/bin/python
import serial
from datetime import datetime
import time
import json
import os
confFile = open("config.json", "r")
conf = json.load(confFile)
confFile.close()
sp = serial.Serial(conf['usbDev'], conf['serialSpeed'])

openSuccess = False
fileNumber = 0
while openSuccess == False:
	try:
		fd = os.open( "radlog-" + str(fileNumber) + ".dat", os.O_RDWR|os.O_CREAT|os.O_EXCL )
	except OSError:
		fileNumber += 1
	else:
		openSuccess = True
		
while True:
	#read will block until there is data
	sp.read()
	os.write(fd, str(int(time.time())) + "\n")
	#flush and sync
	os.fsync(fd)

os.close(fd)
