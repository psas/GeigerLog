#!/usr/bin/python
"""
Logs data from SparkFun SEN 11345 Geiger Counter
"""
import serial
import time
import json
import os
import sys

os.chdir("/home/pi/GeigerLog")
sys.stderr = open("error.log", "w")
CONFFILE = open("config.json", "r")
CONF = json.load(CONFFILE)
CONFFILE.close()
OPENSUCCESS = False
FILENUMBER = 0
while OPENSUCCESS == False:
    try:
        FD = os.open("radlog-" + str(FILENUMBER) + ".dat",
        os.O_RDWR|os.O_CREAT|os.O_EXCL)
    except OSError:
        FILENUMBER += 1
    else:
        OPENSUCCESS = True

SP = serial.Serial(CONF["usbDev"], CONF["serialSpeed"])
try:
    while True:
	#read will block until there is data
	buff = SP.read()
	now = str(int(time.time()))
	for i in range (0, len(buff)):
		os.write(FD, "%s\n" % now)
	#flush and sync
	os.fsync(FD)
finally:
    SP.close()

os.close(FD)
