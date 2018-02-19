unconfirmed_users = ['alice','brain','camdance']
confirmed_users = []

while unconfirmed_users:
	current_users = unconfirmed_users.pop()
	print("Verifying user: "+current_users.title())
	confirmed_users.append(current_users)
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
	print(user.title())


