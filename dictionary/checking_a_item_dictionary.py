print("\nCHECKING IF A KEY EXISTS: TO check if a key exists in  a dictionary,  used the in operator with the if statement.\n()")

person = {"Aplicant_name": "DINESHWAR", # firt key_name = Aplicant_name, and value = DINESHWAR
         "Father_name": "BHARAT",     # second key_name= Father_name, and value = BHARAT
		 "Age":36  ,                  # Third key_name = Age , and value = 36
        } # Dictionary
		 
print("\nThis is Dictionary:",person) # print will be a Dictionary

if "Father_name" in person:        # type1

    print("\nYES, Key is Exists:")  # If key exists in Dictionary, print will be Yes OR otherwise No
	
	
if "CITY" in person:                # type2, If key exists in Dictionary, print will be Yes otherwise No

    print("YES, Key is Exists:")  # If key exists, print will be: Yes/True

else:
	print("\nNO, Key is Exists:\n") # IF  NO Key Exists, print will be: No/False
	
print("Age" in person)       # type3 print will be :True
print("City_name" in person) #type3 print will be :False