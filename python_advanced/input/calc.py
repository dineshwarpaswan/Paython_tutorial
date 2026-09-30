print("\nSIMPLE CALCULATOR WITH HELPS OF:- if..elif\n")


print("Please Selsect an Operation:\n"\
	"+.ADDITION\n"\
	"-.SUBSTRACTION\n"\
	"*.MULTIPLICATION\n"\
	"/.DIVISIONAL\n")

num1 = int(input("Please enter the first value: "))

choice = input("Press for the Operation(+,-,*,/) here: ")

num2 = int(input("Please enter the second value: "))

if choice == "+": 
	print("\nADDITION OF TWO NUMBERs : ", num1,"+",num2, "=", num1 + num2)
			
elif choice == "-":
	print("\nSUBSTRACTION OF TWO NUMBERs :",num1,"-",num2, "=", num1- num2)
			
elif choice == "*":
	print("\nMULTIPLICATION OF TWO NUMBERs :",num1,"*",num2, "=", num1* num2)
			
elif choice == "/":
	print("\nDIVISIONAL OF TWO NUMBERs :",num1,"/",num2, "=", num1/num2)

if (choice !="+") and (choice != "-") and (choice != "*") and (choice != "/"):
	print("\nInvailidation Operator!")

