def make_pizza(size,*toppings):
""" 要制作的pizza"""
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings : ")
for topping in toppings:
	print("- "+topping)
