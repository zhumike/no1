# cars = ['audi','bwm','subaru','toyota']
# for thiscar in cars: 
# 	if thiscar == 'audi':		
# 		print(thiscar.upper())
# 	else:	
# 		print(thiscar.title())
# 
# 
# cars = ['audi','bwm','subaru','toyota']
# user = 'hongqi'
# if user not in cars:
# 	print(user.title() + " car is so poor")
# else:
# 	print(user.title() + " car is great")	


# age = 38
# if age < 4:
# 	print("your level is 0")
# elif age < 18:
# 	print("your level is 1")
# elif age < 38:
# 	print("your level is 2")
# else:
# 	print("your level is 3")


#  遍历
# available_cars = ['audi','bwm','subaru','toyota']
# custmer_requested_cars = ['liulu','audi','huzy']
# for custmer_requested_car in custmer_requested_cars:
# 	if custmer_requested_car in available_cars:
# 		print("adding " + custmer_requested_car)
# 	else:
# 		print("sorry , we don't have  " + custmer_requested_car + ".")


#字典学习
# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])
# new_points = alien_0['points']
# print("you just earned " + str(new_points) +" points!")

 #增加字典键值对
# alien_0 = {'color':'green','points':5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

 #修改字典键值对
# alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
# print("Original x_position: " + str(alien_0['x_position']))
# if alien_0['speed']=='slow':
# 	x_increment = 1
# elif alien_0['speed']=='medium':
# 	x_increment = 2
# else:
# 	x_increment = 3
# alien_0['x_position'] = alien_0['x_position']+x_increment
# print("New x-position ：" + str(alien_0['x_position']))
# 
#遍历字典
# user_0 = {'age':'17','name':'alenande','speed':'medium'}
# for key,value in user_0.items():
# 	print("\nKey:" + key)
# 	print("Value: " + value)
# for qpp,zwe in user_0.items():
# 	print((qpp.title()) + "'s favourite language  is " + (zwe.title()) + ".")
# for key  in user_0.keys():
# 	print((key.title()))

#遍历键
# user_0 = {'age':'17','nadfgme':'alenande','spefsded':'medium'}
# for name in sorted(user_0.keys()):
# 	print((name.title())+" , thank you for taking the poll ")

#遍历值
# user_0 = {'age':'17','nadfgme':'alenande','spefsded':'medium'}
# print("the following lnguages have been mentioned :")
# for znd in user_0.values():
	#print((znd.title()))
	# print(znd)
#把字典的值转换为集合来处理，提出字典中重复的值
# user_0 = {'age':'17','nadfgme':'alenande','spefsded':'medium','azd':'17'}
# print("the following lnguages have been mentioned :")
# for znd in set(user_0.values()):
# 	print(znd)