def classify_age(age):
	age = int(input("Enter your age:"))
	if age <= 0:
		print("You entered an invalid age.")
	elif age <= 12:
		print("You are a child.")
	elif age <= 19:
		print("You are a Teen.")
	elif age <= 64:
		print("You are a Adult.")
	elif age >= 65:
		print("You are a Senior.")
		
classify_age(19)