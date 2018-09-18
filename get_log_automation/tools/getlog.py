import sys
import os
import time
import subprocess
import threading
import shutil
from Util import *
from datetime import datetime


targetdir=r'\\192.168.0.106\log-101'

class GetLog(threading.Thread):

	"""docstring for SendReport"""
	def __init__(self, sn):
		threading.Thread.__init__(self)
		self.sn = sn
		self.mk_document()

	def mkdir(self, path_name): 
		if not os.path.isdir(path_name):
			os.makedirs(path_name)

	def mk_document(self):
#生成日志文件夹
		self.mkdir("FD")
		self.mkdir("FD/" + self.sn)
		self.mkdir("RSS")
		self.mkdir("RSS/" + self.sn)
		self.mkdir("THREAD")
		self.mkdir("THREAD/" + self.sn)
		self.mkdir("Dropbox")
		self.mkdir("Goldeneye")
		self.mkdir("all_log")
		self.mkdir("Hprof")

	def get_android_logs(self, doucment):
		for i in range (0, len(LOG_DIR)):
			output = doucment + "/" + LOG_DOCUMENT[i]
			self.mkdir(output)
			os.system("adb -s " + self.sn + " pull " + LOG_DIR[i] + " " + output)
		if BUGREPORT_SWITCH:
			os.system("adb -s " + self.sn + " bugreport > " + doucment + "/bugreport.txt")
#		os.system("adb -s " + self.sn + " logcat -v threadtime -d -t 10000 > " + doucment + "/logcat.txt")

	def get_tcpdump(self, waittime, doucment):
		try:
			cmd = "adb -s " + self.sn + " shell tcpdump -i any -s 0 -w /data/network.pcap"
			p = subprocess.Popen(cmd)
			time.sleep(waittime) 
			p.terminate()
			self.kill_process("tcpdump")  # make sure tcpdump process is killed!!!!!!!
			os.system("adb -s " + self.sn + " pull /data/network.pcap " + doucment)
			os.system("adb -s " + self.sn + " shell rm -rf /data/network.pcap ")
		except Exception,e:
			print "Get tcpdump maybe exception"

	def kill_process(self, process):
		processes = self.get_processes()
		pid = self.get_process_pid(process, processes)
		os.system("adb -s " + self.sn + " shell kill " + pid)

	def main(self):
		doucment = "all_log/" + self.sn + "-" + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
		doucment_output = "all_log" + "\\" + self.sn + "-" + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
		self.mkdir(doucment)
		sleep_time = GET_LOG_SLEEP_TIME
		if TCPDUMP_SWITCH:
			print "Get %s devices tcpdump!"%self.sn
			self.get_tcpdump(GET_LOG_SLEEP_TIME, doucment)   #抓取tcpdump
			sleep_time = 0
		time.sleep(sleep_time)
		self.get_dropbox_infor()        # 获取dropbox信息
		self.get_goldeneye_infor()		# 获取goldeneye信息
		self.get_android_logs(doucment) # 抓取android_logs
		self.get_meminfor()             # 获取内存信息
		if HPROF_SWITCH:
			self.get_process_dumpheap() # 抓取应用hprof
		#os.system('copyndelete.bat ' + doucment_output)
		#shutil.rmtree(doucment) 

		
	def get_dropbox_infor(self):
		''' 获取dropbox中关键log '''
		mFile = open("Dropbox/" + self.sn + ".txt", 'a')
		mFile.write(str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + "\n")
		mFile.write("-------------------------Begin------------------------------\n")
		dropboxs = os.popen("adb -s " + self.sn + " shell ls  -l /data/system/dropbox").read().split("\n")
		for dropbox in dropboxs:
			for key in DROPBOX_KEYWORD:
				if key in dropbox.lower():
					mFile.write(dropbox + "\n")
		mFile.write("--------------------------End-----------------------------\n")
		mFile.close()
	
	
	def get_goldeneye_infor(self):
		''' 获取dropbox中关键log '''
		mFile = open("Goldeneye/" + self.sn + ".txt", 'a')
		mFile.write(str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + "\n")
		mFile.write("-------------------------Begin------------------------------\n")
		thread_large = os.popen("adb -s " + self.sn + " shell du /data/log/golden_eye_logs/thread_limit").read()
		appmem_large = os.popen("adb -s " + self.sn + " shell du /data/log/golden_eye_logs/appmemlimit").read()
		iowait_large = os.popen("adb -s " + self.sn + " shell du /data/log/golden_eye_logs/iowait_limit").read()
		fd_large = os.popen("adb -s " + self.sn + " shell du /data/log/golden_eye_logs/fdlimit").read()
		mFile.write("thread     " + thread_large + "\n")
		mFile.write("appmem     " + appmem_large + "\n")
		mFile.write("iowait     " + iowait_large + "\n")
		mFile.write("fd     " + fd_large + "\n")
		mFile.write("--------------------------End-----------------------------\n")
		mFile.close()	

	def get_meminfor(self):
		processes = self.get_processes()
		self.get_process_rss(processes)
		self.get_process_fd(processes)
		self.get_process_thread(processes)

	def get_processes(self):
#得到系统进程信息
		return os.popen("adb -s " + self.sn + " shell ps ").read().split("\n")

	def get_process_rss(self, processes):
#得到具体的进程在RAM中所占用的内存大小
		for pro in PROCESS:
			mFile = open("RSS/" + self.sn + "/" + pro + ".txt", 'a')
			for temp in processes:
				if pro in temp:
					mFile.write(str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + ": " + temp + "\n")
					break
			mFile.close()

	def get_process_fd(self, processes):
		for pro in PROCESS:
			pid = self.get_process_pid(pro, processes)
			if pid != "":
				os.system("adb -s " + self.sn + " shell ls -l " + "/proc/" + pid + "/fd >>" + "FD/" +  self.sn + "_" + pro + ".txt")
				mFile = open("FD/" + self.sn + "/" + pro + ".txt", 'a')
				fd_num = len(os.popen("adb -s " + self.sn + " shell ls -l " + "/proc/" + pid + "/fd").read().split("\n"))
				mFile.write(str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + ": " + str(fd_num) + "\n")
				mFile.close()

	def get_process_thread(self, processes):
		for pro in PROCESS:
			pid = self.get_process_pid(pro, processes)
			if pid != "":
				mFile = open("THREAD/" + self.sn + "/" + pro + ".txt", 'a')
				infor = os.popen("adb -s " + self.sn + " shell cat " + "/proc/" + pid + "/status").read().split("\n")
				thread_num = ""
				for temp in infor:
					if "Threads:" in temp:
						thread_num = temp.split("Threads:")[-1].strip()
				mFile.write(str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + ": " + str(thread_num) + "\n")
				mFile.close()

	def get_process_pid(self, pro, processes):
		''' 获取进程pid号 '''
		for temp in processes:
			if pro in temp:
				lists = temp.split(" ")
				for flag in lists[1:]:
					if flag != "" and flag.isdigit():
						return flag
		return ""

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
			print "Wait %d s to get android log!"%GET_LOG_SLEEP_TIME
			self.main()

if __name__ == '__main__':
	mClass = GetLog("3LP7N16930000097")
	mClass.get_dropbox_infor()
