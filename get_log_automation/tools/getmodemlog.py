import sys
import os
import time
import subprocess
import threading
from Util import *
from datetime import datetime

class GetModemLog(threading.Thread):

	"""docstring for SendReport"""
	def __init__(self, sn):
		threading.Thread.__init__(self)
		self.sn = sn
		self.mk_document()

	def mkdir(self, path_name): 
		if not os.path.isdir(path_name):
			os.makedirs(path_name)

	def mk_document(self):
		self.mkdir("modem_log")
		self.mkdir("modem_log/" + self.sn)

	def main(self):
		time.sleep(GET_MODEM_LOG_SLEEP_TIME)
		self.get_modemlog()             # ץȡmodem log

	def get_modemlog(self):
		print "Pull devices %s modem log .... \n "%self.sn
		document = "modem_log/" + self.sn + "_" + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
		self.mkdir(document)
		os.system("adb -s " + self.sn + " pull " + MODEM_LOG_DIR + " " + document)
		

	def run(self):
		while True:
			print "Wait %d s to get modem_log!"%GET_MODEM_LOG_SLEEP_TIME
			self.main()

if __name__ == '__main__':
	mClass = GetModemLog("3LP7N16930000024")
	mClass.run()
