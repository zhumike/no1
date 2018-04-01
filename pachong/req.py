import requests
"""发送网页请求，获取响应状态码，打印获取到的信息"""
# r = requests.get('http://book.douban.com/subject/1084336/comments/')
# print(r.status_code)
# print(r.text)


r = requests.get('https://www.baidu.com/img/bd_logo1.png')
with open('E:\\codeindex\\zhu\\no1\\pachongbaidu.png', 'wb') as fp:
     fp.write(r.content)