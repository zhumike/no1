responses = {}
pflag= True
while pflag:
	name = input("\nWhat's is your name ? ")
	response= input("Which mountain would you like to climb someday? ")
#把答案存储在字典中
	responses[name] = response

#查看其余人是否要参与调查
	repeat = input("Would you like to let another persion respond ?(yes/no) ")
	if repeat == 'no':
 		pflag = False
 #调查结束
print("\n --- POLL results ---")
for name,response in responses.items():
	print(name+"would like to climb "+response+".")


