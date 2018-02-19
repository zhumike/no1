import os

# 字节bytes转化kb\m\g
# def formatSize(bytes):
#     try:
#         bytes = float(bytes)
#         kb = bytes / 1024
#     except:
#         print("传入的字节格式不对")
#         return "Error"

#     if kb >= 1024:
#         M = kb / 1024
#         if M >= 1024:
#             G = M / 1024
#             return "%fG" % (G)
#         else:
#             return "%fM" % (M)
#     else:
#         return "%fkb" % (kb)

# 获取文件大小
# def getDocSize(path):
#     try:
#         size = os.path.getsize(path)
#         return formatSize(size)
#     except Exception as err:
#         print(err)
# def file_list_show(path):		
#files = os.listdir("D:\zhu\log")
#dirs = os.listdir("D:\zhu\log")

# 输出所有文件和文件夹
# 
# os.walk("D:\zhu\log")
# for root,dir,filename in os.walk('/log/')
#    print (root,dirs,files)
# # if '__name__'=='__main__':
# #     file_list_show("/log/")

path='D:\zhu\log'
for root,dirs,files in os.walk(path,False):
    print("Root = ", root, "dirs = ", dirs, "files = ", files)
print("hello")