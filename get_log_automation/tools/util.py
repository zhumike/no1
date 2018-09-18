import os

LOG_DIR = ["/data/hisi_logs", "/data/log/android_logs", "/data/log/isp-log","/data/system/dropbox", "/data/log/reliability/goldeneye", "/sdcard/Android/data/com.huawei.ims/", "/data/data/com.huawei.ims", "/data/log/LogService/901","/data/log/jank","/data/log/input-log","/data/log/charge-log","/data/log/sleeplog","/data/log/gps_log","/data/gps","/data/tombstones","/data/log/mdm_dbg.txt"]
LOG_DOCUMENT = ["hisi_logs", "android-log","isp-log","dropbox", "golden_eye_logs", "sdcard_ims", "data_ims", "901","jank","input-log","charge-log","sleep-log","gps_log","gps","tombstones","mdm_dbg"]
PROCESS = ["com.android.browser", "com.android.systemui", "system_server", "com.android.mms", "HwCamCfgSvr"]
HPROF_PROCESS = ["com.android.browser"]
DROPBOX_KEYWORD = ["crash", "tombstone", "anr", "watchdog", "restart", "lowmem"]
MODEM_LOG_DIR = "/sdcard/log/modem/balonglte"
MODEM_LOG_DIR_DEL = "/sdcard/log/modem/balonglte/*"

HPROF_SWITCH = True         # hprof 开关
BUGREPORT_SWITCH = False     # bugreport 开关
TCPDUMP_SWITCH = True        # tcpdump 开关
GET_MODEM_SWITCH = True      # 获取modem log

GET_LOG_SLEEP_TIME = 60    # 抓取log间隔等待时间
GET_MODEM_LOG_SLEEP_TIME = 7200 # 抓取modemlog间隔等待时间
GET_SYSTEM_LOG_SLEEP_TIME = 60
GET_TCPDUMP_SLEEP_TIME = 3600
