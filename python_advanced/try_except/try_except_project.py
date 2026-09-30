# try block: <--iske andar woh code likha jata hai jisme error aane ki change hota hai.")

# except block: <--Agar try ke andar koi error aaye , toh code yahan jump kar jata aur crash hone ke bajaye aapka likha hua messege print kar deta hai.\n")

# <----Fortunately, errors can be handled in python
try: 
	number = int(input("Plese Enter The One Digit: "))
	result = 10 / number
	print("Result will be: ",result)
	
except ZeroDivisionError:
	print("\nError(Galti): You can not divide to Zero!") # error <-alert message keliye used kiya jata hai

except ValueError:
	print("\nError(Galti): You can not divide for the string value, Please only 1 to 9 number!") # error <-alert message keliye used kiya jata hai
