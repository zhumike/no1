from pandas import *
import pandas as pd
import matplotlib.pyplot as plt
# obj=Series([4,7,-5,3],index=['d','b','a','c'])
# print(obj)
# print(obj.values)

# data = {'state':['ohio','ohji','neiou','swe'],'year':[2000,2345,3456,1234],'pop':[1.5,1.7,3.6,6.9]}
# fram=DataFrame(data,columns=['year','state','pop'])
# print(fram)
# 
# obj = Series(['c','c','c','d','f','e','a','a','j','z'])
# uniq=obj.unique()

# print(obj.value_counts())

# data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
# print(data)
# print(data.index)
# print(data['b'])
# result = pd.read_csv('E:/codeindex/zhu/no1/dataanalsys/pydata-book/examples/ex1.csv')
# print(result)
# import requests
# import json
# url = 'http://www.baidu.com'
# resp = requests.get(url)
# data = json.loads(resp.text)
# print(resp)



result=pd.read_csv('E:/codeindex/zhu/no1/dataanalsys/pydata-book/examples/ex1.csv')
# print(result)
# print(result['a'])
s=result['a']
dq=Series(s)
print(dq.values)
print(dq.index)
# data = {'state':['ohio','ohji','neiou','swe'],'year':[2000,2345,3456,1234]}
# fram=DataFrame(data)
# print(data['state'])

# inputvalue = data['state']
# v2=data['year']
# plt.title("data show",fontsize=24)
# plt.xlabel("value info",fontsize=14)
# plt.ylabel("year info",fontsize=14)
# plt.plot(inputvalue,v2)
# plt.scatter(inputvalue,v2,c=(0.9,0,0),edgecolor='none',s=40)
# plt.show()