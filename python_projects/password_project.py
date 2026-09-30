import re

#Password Strength Cheacker

# Password Strength Cheacker Conditions:
# Min 8 char, digit, upper case, lower case & special

def check_password_strength(password):

	if len(password) < 8 : # lenth of password

		return "Weak: Password must be at least 8 char!"

	if  not any(char.isdigit() for char in password):

		return "Weak: Password must conatain a digit!"

	if not any(char.isupper() for char in password):

		return "Weak: Password must conatain an Upper Char!"

	if not any(char.islower() for char in password):

		return "Weak. password must conatain a Lower Char!"

	if not re.search(r'[!@#$%^&*(){}?()<>.?,]', password):

		return "Medium:  password must conatain a Special Char!"

	return "Strong: Your password is secured"

def password_checker():

	print("Welcome to the password Strength Cheacker")

	while True:


		password = input("Enter Your password (or type 'exit' to quit): ")

		if password.lower() == 'exit':

			print("Thank you for using this tool")
			break

		result = check_password_strength(password)
		print(result)

# Run the password checker tool
if __name__== "__main__":
        password_checker()





















