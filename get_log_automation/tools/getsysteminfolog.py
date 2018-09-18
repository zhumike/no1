import sys
import os
import time
import subprocess
import threading
from Util import *
from datetime import datetime

class GetsysteminfoLog(threading.Thread):

	"""docstring for SendReport"""
	def __init__(self, sn):
		threading.Thread.__init__(self)
		self.sn = sn
		self.mk_document()

	def mkdir(self, path_name): 
		if not os.path.isdir(path_name):
			os.makedirs(path_name)

	def mk_document(self):
		self.mkdir("systeminfo_log")
		self.mkdir("systeminfo_log/" + self.sn)

	def main(self):
		time.sleep(GET_SYSTEM_LOG_SLEEP_TIME)
		self.get_systeminfolog()             # 抓取modem log
#		self.get_process_dumpheap()

	def get_systeminfolog(self):
		print "Pull devices %s system info log .... \n "%self.sn
		document = "systeminfo_log/" + self.sn + "_" + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
		self.mkdir(document)
		os.system("adb -s " + self.sn + " shell dumpsys meminfo -oom " + "> " + document + "/meminfooom")
		os.system("adb -s " + self.sn + " shell dumpsys cpuinfo " + "> " +document + "/cpuinfo")
		os.system("adb -s " + self.sn + " shell dumpsys powerprofile " + "> " + document + "/powerprofile")
		os.system("adb -s " + self.sn + " shell dumpsys ioinfo " + "> " + document + "/ioinfo")
		os.system("adb -s " + self.sn + " shell cat /proc/vmstat " + "> " + document + "/vmstat")
		os.system("adb -s " + self.sn + " shell dumpsys meminfo " + "> " + document + "/meminfo")		

	def get_process_dumpheap(self):
		''' 获取应用的hprof '''
		for process in HPROF_PROCESS:
			os.system("adb -s " + self.sn + " shell setenforce 0")
			os.system("adb -s " + self.sn + " shell am dumpheap " + process + " /sdcard/" + process)
			time.sleep(10)
			hprof_name = self.sn + str(datetime.now().strftime('%Y-%m-%d-%H-%M')) + "_" + process + ".hprof"
			os.system("adb -s " + self.sn + " pull /sdcard/" + process + " ./Hprof/" + hprof_name)

	def run(self):
		while True:
			print "Wait %d s to get systeminfo_log!"%GET_SYSTEM_LOG_SLEEP_TIME
			self.main()

if __name__ == '__main__':
	mClass = GetModemLog("3LP7N16930000024")
	mClass.run()
