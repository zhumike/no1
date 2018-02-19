# message = input(" Tell me 好吧，and I will repeat it back to you:")
# print(message)

# number = input("Enter a number ,and I will tell you if it is even or odd:")
# number = int(number)
# if number < 0:
# 	print("\n The number "+str(number)+" is error .")
# elif number%2==0:
# 	print("\n The number "+str(number)+" is even .")
# else:
# 	print("\n The number "+str(number)+" is odd .")
promp = "\n Tell me something ,and I will repeat it back to you :"
promp+="\n Enter 'quit' to end the program ."
message=" "
while message != 'quit':
	message = input(promp)
	if message != 'quit':
		print(message)

