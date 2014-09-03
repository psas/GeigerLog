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
dataFile = open(conf['dataFile'],"a")

while True:
	#read will block until there is data
	sp.read()
	dataFile.write(str(int(time.time())) + "\n")
	#flush and sync
	dataFile.flush()
	os.fsync(dataFile)

dataFile.close()

