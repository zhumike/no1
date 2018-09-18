import os,sys
import shutil
import time




def getDevicesList():
	os.system("adb devices")
	return list(map(lambda x: x.split("\t")[0], os.popen("adb devices").readlines()[1:-1]))

def cur_file_dir():
	path = sys.path[0]
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)


def get_adb_logs(log_path):
	for i in range(10000):
		for device in getDevicesList():
			#os.system("adb -s " + device + " shell setprop persist.adb.trace_mask all")
			time.sleep(30)
			os.system("adb -s %s pull /data/adb/ %s"%(device,os.path.join(log_path,device)))
			os.system("adb -s " + device + " shell rm -rf /data/adb ")

def run_reset_user(log_path):
	for i in range(10000):
		for device in getDevicesList():
			os.system("adb -s " + device + " wait-for-device")
			os.system("adb -s " + device + " reboot")
			f=open(device+".txt",'w')
			f.write("had reboot " + str(i) + " times " + time.strftime('%Y-%m-%d',time.localtime(time.time())))
			f.write("\n")
			time.sleep(30)
			os.system("adb -s %s pull /splash2/LogService/901/ %s"%(device,os.path.join(log_path,device)))
			os.system("adb -s %s pull /data/hisi_logs/ %s"%(device,os.path.join(log_path,device)))
			os.system("adb -s %s pull /splash2/boot_fail/ %s"%(device,os.path.join(log_path,device)))
			os.system("adb -s " + device + " reboot resetuser")
			time.sleep(90)
			f.write("had resetuser " + str(i) + " times " + time.strftime('%Y-%m-%d',time.localtime(time.time())))
			f.close()

			


if __name__=="__main__":

	log_path = os.path.join(cur_file_dir(),"log")
	print(log_path)

	if not os.path.exists(log_path):
		os.mkdir(log_path)
	get_adb_logs(log_path)


