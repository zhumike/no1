# def make_shirt(chima,ziyang):
# 	print("The T-shirt size is "+chima)
# 	print("The T-shirt info is "+ziyang)
# make_shirt(chima='180',ziyang='nike')
def greet_users(names):
	"""xxxx"""
	for name in names:
		msg="Hello, "+name.title()+"!"
		print(msg)
usernames = ['mike','lili','owen']
greet_users(usernames)
