from pandas import *
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

data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
print(data)
print(data.index)
print(data['b'])