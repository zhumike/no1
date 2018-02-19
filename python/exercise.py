#练习
# rivers={'yangzi river':'China','nile river':'egypt','henhe river':'India'}
# for heliu,guojia in rivers.items():
# 	print("The "+heliu+" runs through "+(guojia.title()))
# for he in rivers.keys():
# 	print(he)
# for guo in rivers.values():
# 	print((guo.title()))

# rivers={'yangzi river':'China','nile river':'egypt','henhe river':'India'}
# country = ['China','America','France']
# for li in rivers.values():
# 	print((li.title()))
# 	if li in country:
# 		print("Thank  you "+li.title())
# 	else:
# 		print(li.title()+" please come")

#嵌套字典
#列表中嵌套字典
# aliens=[]
# for alien_number in range(30):
# 	new_alien={'color':'green','points':'5','speed':'slow'}
# 	aliens.append(new_alien)
# for alien in aliens[:5]:
# 	print(alien)
# print("good")
# print("The total number of aliens: "+str(len(aliens)))
  

 #字典中嵌套列表 
# pizza = {'crust':'thick','toppings':['mushroom','extra cheese']}
# print("You ordered a "+pizza['crust']+" crust pizza"+" with the following toppings")
# for topping in pizza['toppings']:
# 	print("\t" + topping)


#字典中嵌套字典
users={'znc':{'first':'albert','last':'einstein','location':'princeton'},'mcurie':{'first':'marie','last':'curie','location':'paris'}}
for username ,userinfo in users.items():
	print("\n Username: "+username)
	full_name=userinfo['first']+" "+userinfo['last']
	location = userinfo['location']
	print("\t Full name: "+full_name.title())
	print("\t Locatioin: "+location.title())
