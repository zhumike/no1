# >>> a = 3
# >>> print(a)
# 3
# >>> print(id(a))
# 1709265760
# >>> b=3
# >>> print(id(b))
# 1709265760
# >>> c =3
# >>> print(id(c))
# 1709265760
# >>> c=(3,6,7)
# >>> print(c)
# (3, 6, 7)
# >>> print(id(c))
# 2314031463376
# >>> csd = "dddffg"
# >>> print(id(csd))
# 2314031637200
# >>> asd = "dddffg"
# >>> print(id(asd))
# 2314031637200
# >>> s = "asddddgfdgfdgfd"
# >>> q= set(s)
# >>> q= list(q)
# >>> q.sort(reverse=False)
# >>> res = "".join(q)
# >>> print(res)
# adfgs
# >>> sum =lambda a,b:a*b
# >>> print(sum(5,4))
# 20
# >>>
# from collections import Counter
# a = "dfmdfmvfldvk;kmdkdsm;nvkfvfkd"
# res = Counter(a)
# print(res)


# import re
# a = "not 404 found 张三 98 北京"
# list = a.split(" ")
# print(list)
# res = re.findall('\d+|[a-zA-Z]+',a)
# for i in res:
# 	if i in list:
# 		list.remove(i)
# new_str=" ".join(list)
# print(res)
# print(new_str)

# a = [1,2,3,4,5,6,7,5,4,5]
# def fn(a):
# 	return a%2==1
# newlist = filter(fn,a)
# newlist=[i for i in newlist]
# print(newlist)

#使用sort，sorted对排序的影响
# list = [0,-1,3,-10,5,9]
# list.sort(reverse=False)
# print("list.sort在list基础上修改,无返回值 ",list)

# list2 = [0,-1,3,-10,5,9]
# res=sorted(list,reverse=False)
# print("sorted有返回值,是新的list",list2)
# print("返回值 ",res)


#嵌套字典排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
# print(foo)
# a=sorted(foo,key=lambda x:x["age"],reverse=True)
# print(a)
# a=sorted(foo,key=lambda x:x["name"])
# print(a)

s=["ab","abc","a","djkj"]
b=sorted(s,key=lambda x:len(x))
print(b,s)
s.sort(key=len)
print(s)

